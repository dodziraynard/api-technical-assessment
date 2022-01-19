from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    weight: float
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: Optional[str] = None
    weight: Optional[float] = None
    description: Optional[str] = None


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
