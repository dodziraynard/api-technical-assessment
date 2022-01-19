from app import crud, schemas
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Returns an item with the specified id or None if it does not exist."""
    item = crud.get_item(db, item_id=item_id)
    return item


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Creates and returns an item in the database using the posted data.."""
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item: schemas.ItemUpdate,
                item_id: int,
                db: Session = Depends(get_db)):
    """Updates and retuns an item with the specified id or returns None if it does not exist."""
    db_item = crud.get_item(db, item_id=item_id)
    if not db_item:
        return db_item
    return crud.update_item(db=db, item_id=item_id, item=item)
