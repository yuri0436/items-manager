from enum import Enum
from typing import Optional
from schemas import ItemCreate


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


#商品
class Item:
    def __init__(
        self,
        id: int,
        name: str,
        price: int,
        description: Optional[str],
        category:ItemCategory,
        status:ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.status = status


#テスト用アイテム
items = [
    Item(1, "Windows PC", 100000, "デスクトップPCです。", ItemCategory.PC.param, ItemStatus.ON_SALE),
    Item(2, "スラムダンク10巻", 500, "漫画です。", ItemCategory.BOOK.param, ItemStatus.ORIGINAL_PRICE),
    Item(3, "眼鏡", 7000, "レディース用メガネフレームです。", ItemCategory.CLOTHES.param, ItemStatus.SOLD_OUT),
]


def find_all():
    return items


def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None


def find_by_name(name: str):
    filtered_items = []
    
    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items


def create(item_create: ItemCreate):
    new_item = Item(
        len(items) + 1,
        item_create.name,
        item_create.price,
        item_create.description,
        ItemCategory.get_by_id(item_create.category),
        ItemStatus.get_by_id(item_create.status)
    )
    items.append(new_item)
    return new_item


def update(id: int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name", item.name)
            item.price = item_update.get("price", item.price)
            item.description = item_update.get("description", item.description)

            category = item_update.get("category")
            if category is not None:
                item.category = ItemCategory.get_by_id(category)
            status = item_update.get("status")
            if status is not None:
                item.status = ItemStatus.get_by_id(status)  
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None