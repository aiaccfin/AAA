from fastapi import APIRouter, HTTPException, Depends

from passlib.context import CryptContext # type: ignore

from app.models.m_user import UserCreate, User, TokenResponse
from app.db.x_mg_conn import users_collection


router = APIRouter()


@router.post("/register", response_model=User)
async def create_user(user: UserCreate):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user.password_hash = pwd_context.hash(user.password_hash)
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_dict = user.model_dump()
    new_user = await users_collection.insert_one(user_dict)
    return {"id": str(new_user.inserted_id), **user_dict}


