from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class ItemInfo(Enum):
    def __init__(self, id, param):
        self.id = id
        self.param = param

    #idとparamを連結した文字列を返却
    @property
    def tag(self):
        return "{}:{}".format(self.id, self.param)
    
    #全ての列挙型メンバーを取得
    @classmethod
    def members_as_list(cls):
        # Order dictionary -> list
        return [*cls.__members__.values()]
    
    # idを指定して取得
    @classmethod
    def get_by_id(cls, id: int):
        for c in cls.members_as_list():
            if id == c.id:
                return c
        # default
        return None


#商品カテゴリー(大分類)
class ItemCategory(ItemInfo):
    BOOK = (1, "本・コミック・雑誌")
    DVD = (2, "DVD・ミュージック・ゲーム")
    ELECTRICAL = (3, "電化製品")
    PC = (4, "パソコン関連")
    FOOD = (5, "食品・飲料")
    DRUG = (6, "薬")
    CLOTHES = (7, "服・服飾雑貨")
    OTHER = (8, "その他")


#商品ステータス
class ItemStatus(ItemInfo):
    ON_SALE = (1, "セール中")
    SOLD_OUT = (2, "売り切れ")
    ORIGINAL_PRICE = (3, "定価")



class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: int = Field(ge=1, le=8, examples=["1:BOOK, 2:DVD, 3:ELECTRICAL, 4:PC, 5:FOOD, 6:DRUG, 7:CLOTHES, 8:OTHER"])
    status: int = Field(ge=1, le=3, examples=["1:ON_SALE, 2:SOLD_OUT, 3:ORIGINAL_PRICE"])
    # category: int = Field(ge=1, le=item_cruds.ItemCategory.__len__(), examples=["商品カテゴリ"])
    # status: int = Field(ge=1, le=item_cruds.ItemStatus.__len__(), examples=["商品ステータス"])


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=20, examples=["PC"])
    price: Optional[int] = Field(None, gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: Optional[int] = Field(None, ge=1, le=8, examples=["1:BOOK, 2:DVD, 3:ELECTRICAL, 4:PC, 5:FOOD, 6:DRUG, 7:CLOTHES, 8:OTHER"])
    status: Optional[int] = Field(None, ge=1, le=3, examples=["1:ON_SALE, 2:SOLD_OUT, 3:ORIGINAL_PRICE"])


class ItemResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[100000])
    description: Optional[str] = Field(None, examples=["2023年の夏モデルです。"])
    category: ItemCategory = Field(examples=["4,PC"])
    status: ItemStatus = Field(examples=["1,ON_SALE"])

