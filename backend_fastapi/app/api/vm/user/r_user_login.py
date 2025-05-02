import datetime, jwt, os
from jwt import PyJWTError
from fastapi import APIRouter, HTTPException, Depends
from app.db.x_mg_conn import users_collection, verification_collection
from app.utils.gmail_api_sender import generate_and_send_verification_code
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

from app.models.m_login import TokenResponse, LoginRequest, LoginVerification
from app.db.x_mg_conn import users_collection

@router.post("/login")
async def login(request: LoginRequest):
    print(request.email)
    user = await users_collection.find_one({"email": request.email})
    
    if not user.get("is_verified", False) and not user.get("email_verified", False):
        await generate_and_send_verification_code(user["email"])
        raise HTTPException(
            status_code=403,
            detail="Email not verified. A new verification code has been sent to your email."
        )

        # Email is verified, login is successful
    return {"message": "Login successful"}

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
    
    
    

@router.post("/login/verify", response_model=TokenResponse)
async def verify_login_code(data: LoginVerification):
    # Check if the code is correct
    code_doc = await verification_collection.find_one({
        "email": data.email,
        "code": data.code
    })

    if not code_doc:
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    # Get the user again
    user = await users_collection.find_one({"email": data.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Mark the user as verified (optional - or you can leave this only in registration)
    await users_collection.update_one(
        {"email": data.email},
        {"$set": {"email_verified": True}}
    )

    # Remove used code
    await verification_collection.delete_many({"email": data.email})

    # Create JWT token
    token_data = {
        "sub": user["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=ACCESS_TOKEN_EXPIRE_MINUTES),
        "primary_role":  user.get("primary_role", []),
        "primary_group": user.get("primary_group", []),
        "roles": [str(role) for role in user.get("roles", [])],
        "groups": [str(group) for group in user.get("groups", [])],
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
