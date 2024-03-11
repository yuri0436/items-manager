from fastapi import APIRouter, Path, Query, HTTPException
from starlette import status
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse


router = APIRouter(prefix="/items", tags=["items-manager"])


#全ての商品を検索
@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all():
    return item_cruds.find_all()


#商品idで検索
@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def find_by_id(id: int = Path(gt=0)):
    found_item = item_cruds.find_by_id(id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


#商品名で検索
@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_by_name(name: str = Query(min_length=2, max_length=20)):
    found_item = item_cruds.find_by_name(name)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


#商品を追加
@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(item_create: ItemCreate):
    return item_cruds.create(item_create)


#対象商品の登録内容を更新
@router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update(item_update: ItemUpdate, id: int = Path(gt=0)):
    update_item = item_cruds.update(id, item_update)
    if not update_item:
        raise HTTPException(status_code=404, detail="Item not updated")
    return update_item


#対象商品を削除
@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(id: int = Path(gt=0)):
    deleted_item = item_cruds.delete(id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item