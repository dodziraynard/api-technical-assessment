from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas

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
    item = crud.get_item(db, item_id=item_id)
    return item


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item: schemas.ItemUpdate,
                item_id: int,
                db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if not db_item:
        return HTTPException(404, detail="Item not found.")
    return crud.update_item(db=db, item_id=item_id, item=item)
