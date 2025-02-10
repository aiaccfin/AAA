from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from app.db import pg_conn
from seed_data.storage_in_memory import my_posts
from schemas import t_schema
from app.db import pg_crud

router = APIRouter()

@router.get('/posts')
async def index(): return my_posts


@router.get("/", response_model=list[t_schema.Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(pg_conn.get_db)):
    items = pg_crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=t_schema.Item)
def read_item(item_id: int, db: Session = Depends(pg_conn.get_db)):
    db_item = pg_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/p", response_model=t_schema.Item)
def create_item(item: t_schema.ItemCreate, db: Session = Depends(pg_conn.get_db)):
    return pg_crud.create_item(db=db, item=item)