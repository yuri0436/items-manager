from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


#商品カテゴリー(大分類)
class ItemCategory(Enum):
    BOOK = "BOOK"
    DVD = "DVD"
    ELECTRICAL = "ELECTRICAL"
    PC = "PC"
    FOOD = "FOOD"
    DRUG = "DRUG"
    CLOTHES = "CLOTHES"
    OTHER = "OTHER"


#商品ステータス
class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"
    ORIGINAL_PRICE = "ORIGINAL_PRICE"


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: ItemCategory = Field(examples=["BOOK, DVD, ELECTRICAL, PC, FOOD, DRUG, CLOTHES, OTHER"])
    status: ItemStatus = Field(examples=["ON_SALE, SOLD_OUT, ORIGINAL_PRICE"])


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=20, examples=["PC"])
    price: Optional[int] = Field(None, gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: Optional[ItemCategory] = Field(None, examples=["BOOK, DVD, ELECTRICAL, PC, FOOD, DRUG, CLOTHES, OTHER"])
    status: Optional[ItemStatus] = Field(None, examples=["ON_SALE, SOLD_OUT, ORIGINAL_PRICE"])


class ItemResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: ItemCategory = Field(examples=["PC"])
    status: ItemStatus = Field(examples=["ON_SALE"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str = Field(min_length=2, examples=["user1"])
    password: str = Field(min_length=8, examples=["test1234"])


class UserResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    username: str = Field(min_length=2, examples=["user1"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str