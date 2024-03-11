from typing import Optional
from pydantic import BaseModel, Field
from cruds import item as item_cruds

class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: int = Field(ge=1, le=8, examples=["1:BOOK, 2:DVD, 3:ELECTRICAL, 4:PC, 5:FOOD, 6:DRUG, 7:CLOTHES, 8:OTHER"])
    status: int = Field(ge=1, le=3, examples=["1:ON_SALE, 2:SOLD_OUT, 3:ORIGINAL_PRICE"])
    # category: int = Field(ge=1, le=item_cruds.ItemCategory.__len__(), examples=["商品カテゴリ"])
    # status: int = Field(ge=1, le=item_cruds.ItemStatus.__len__(), examples=["商品ステータス"])

