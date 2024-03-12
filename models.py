from datetime import datetime
from heapq import nlargest
from schemas import ItemCategory, ItemStatus
from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    category = Column(Enum(ItemCategory), nullable=False)
    status = Column(Enum(ItemStatus), nullable=False, default=ItemStatus.ORIGINAL_PRICE)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())