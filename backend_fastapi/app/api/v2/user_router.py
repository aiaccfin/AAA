from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from app.db import pg_conn, pg_crud
from schemas import t_schema, user_schema
from app.db import pg_table
from utils import u_hash

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


@router.post("/new/", response_model=user_schema.UserOut, status_code=201)
def create_user(user: user_schema.UserCreate, db: Session = Depends(pg_conn.get_db)):
    hashed_password = u_hash.hash_password(user.password)
    new_user = pg_table.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

