from fastapi import APIRouter, Body
from cruds import item as item_cruds
import routers


router = APIRouter(prefix="/items", tags=["items-manager"])


#全ての商品を検索
@router.get("")
async def find_all():
    return item_cruds.find_all()


#商品idで検索
@router.get("/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)


#商品名で検索
@router.get("/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)


#商品を追加
@router.post("")
async def create(item_create=Body()):
    return item_cruds.create(item_create)


#対象商品の登録内容を更新
@router.put("/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)


#対象商品を削除
@router.delete("/{id}")
async def delete(id: int):
    return item_cruds.delete(id)