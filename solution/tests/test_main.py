import unittest
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app.main import app, get_db

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup test DB
test_db = "test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{test_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Inject test DB settings into app.
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.test_data = {
            "name": "Item 1",
            "weight": 1,
            "description": "Description",
        }

    def tearDownClass():
        print("\n Destroying Test Database.")
        if Path.exists(BASE_DIR / test_db):
            Path(BASE_DIR / test_db).unlink(missing_ok=False)

    def test_create_item(self):
        response = client.post(
            "/items/",
            json=self.test_data,
        )
        self.assertEqual(response.status_code, 200)
        expected = self.test_data.copy()
        expected.update({"id": 1})
        self.assertEqual(response.json(), expected)

    def test_require_name(self):
        mod_test = self.test_data.copy()
        mod_test.update({"name": None})
        response = client.post(
            "/items/",
            json=mod_test,
        )
        self.assertNotEqual(response.status_code, 200)

    def test_require_weight(self):
        mod_test = self.test_data.copy()
        mod_test.update({"weight": None})
        response = client.post(
            "/items/",
            json=mod_test,
        )
        self.assertNotEqual(response.status_code, 200)

    def test_description_optional(self):
        mod_test = self.test_data.copy()
        mod_test.update({"description": None})
        response = client.post(
            "/items/",
            json=mod_test,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_item(self):
        response = client.post("/items/", json=self.test_data)
        self.assertEqual(response.status_code, 200)
        new_id = response.json().get("id")
        get_res = client.get(f"/items/{new_id}")
        self.assertEqual(get_res.status_code, 200)

    def test_update_item(self):
        response = client.post("/items/", json=self.test_data)
        self.assertEqual(response.status_code, 200)
        new_id = response.json().get("id")
        get_res = client.put(f"/items/{new_id}",
                             json={
                                 "name": "New Name",
                                 "description": None,
                                 "weight": 44
                             })
        self.assertEqual(
            get_res.json(), {
                "name": "New Name",
                "description": None,
                "weight": 44,
                "id": get_res.json().get("id")
            })
        self.assertEqual(get_res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
