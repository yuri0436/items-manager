from email.policy import default
from enum import Enum
from typing import Optional


#商品のカテゴリ(大分類)
class ItemCategory(Enum):
    BOOK = "本・コミック・雑誌"
    DVD = "DVD・ミュージック・ゲーム"
    ELECTRICAL = "電化製品"
    PC = "パソコン関連"
    FOOD = "食品・飲料"
    DRUG = "薬"
    CLOTHES = "服・服飾雑貨"
    OTHER = "その他"


class ItemStatus(Enum):
    ON_SALE = "セール中"
    SOLD_OUT = "売り切れ"
    ORIGINAL_PRICE = "定価"


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


items = [
    Item(1, "Windows PC", 100000, "デスクトップPCです。", ItemCategory.PC, ItemStatus.ON_SALE),
    Item(2, "スラムダンク10巻", 500, "漫画です。", ItemCategory.BOOK, ItemStatus.ORIGINAL_PRICE),
    Item(3, "眼鏡", 7000, "レディース用メガネフレームです。", ItemCategory.CLOTHES, ItemStatus.SOLD_OUT),
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


def create(item_create):
    new_item = Item(
        len(items) + 1,
        item_create.get("name"),
        item_create.get("price"),
        item_create.get("description"),
        ItemCategory[item_create.get("category")],
        ItemStatus.ORIGINAL_PRICE
    )
    items.append(new_item)
    return new_item


def update(id: int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name", item.name)
            item.price = item_update.get("price", item.price)
            item.description = item_update.get("description", item.description)
            item.category = ItemCategory[item_update.get("category", item.category)]
            item.status = ItemStatus[item_update.get("status", item.status)]
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None