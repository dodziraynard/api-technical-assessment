from sqlalchemy import Column, Float, Integer, String

from .db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    weight = Column(Float(precision=2))
    description = Column(String(), index=True, nullable=True)
