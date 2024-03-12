from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse
from database import get_db


DbDependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/items", tags=["items-manager"])


#全ての商品を検索
@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    return item_cruds.find_all(db)


#商品idで検索
@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DbDependency, id: int = Path(gt=0)):
    found_item = item_cruds.find_by_id(db, id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


#商品名で検索
@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_by_name(db: DbDependency, name: str = Query(min_length=2, max_length=20)):
    found_item = item_cruds.find_by_name(db, name)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


#商品を追加
@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDependency, item_create: ItemCreate):
    return item_cruds.create(db, item_create)


#対象商品の登録内容を更新
@router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update(db: DbDependency, item_update: ItemUpdate, id: int = Path(gt=0)):
    update_item = item_cruds.update(db, id, item_update)
    if not update_item:
        raise HTTPException(status_code=404, detail="Item not updated")
    return update_item


#対象商品を削除
@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(db: DbDependency, id: int = Path(gt=0)):
    deleted_item = item_cruds.delete(db, id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item