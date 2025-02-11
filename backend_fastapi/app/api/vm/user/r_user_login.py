import datetime, jwt, os
from jwt import PyJWTError
from fastapi import APIRouter, HTTPException, Depends
router = APIRouter()

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

from passlib.context import CryptContext # type: ignore
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1))

from app.models.m_login import TokenResponse, LoginRequest
from app.db.x_mg_conn import users_collection

@router.post("/login")
async def login(request: LoginRequest):
    print(request.username)
    user = await users_collection.find_one({"name": request.username})
    
    if not user or not pwd_context.verify(request.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT token
    token_data = {
        "sub": user["name"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=ACCESS_TOKEN_EXPIRE_MINUTES),
        "primary_role":  user.get("primary_role", []),
        "primary_group": user.get("primary_group", []),
        "roles": [str(role) for role in user.get("roles", [])],  # Ensure list of strings
        "groups": [str(group) for group in user.get("groups", [])],
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
async def get_user_info(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = await users_collection.find_one({"name": payload["sub"]})
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "username": user["name"],
            "email": user.get("email", ""),
            "primary_role_id":  user.get("primary_role", []),
            "primary_group_id": user.get("primary_group", []),
            "roles": [str(role) for role in user.get("roles", [])],  # Ensure list of strings
            "groups": [str(group) for group in user.get("groups", [])],
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except PyJWTError:  # ✅ Correct exception name
        raise HTTPException(status_code=401, detail="Invalid or expired token")