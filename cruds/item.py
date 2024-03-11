from fastapi import Body
from typing import Optional
from schemas import ItemCategory, ItemStatus, ItemCreate, ItemUpdate


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


def update(id: int, item_update: ItemUpdate):
    for item in items:
        if item.id == id:
            item.name = item.name if item_update.name is None else item_update.name
            item.price = item.price if item_update.price is None else item_update.price
            item.description = item.description if item_update.description is None else item_update.description

            category_number = item.category.id if item_update.category is None else item_update.category
            item.category = ItemCategory.get_by_id(category_number)
            status_number = item.status.id if item_update.status is None else item_update.status
            item.status = ItemStatus.get_by_id(status_number)
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None