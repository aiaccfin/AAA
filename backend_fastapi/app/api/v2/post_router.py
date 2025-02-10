from seed_data.storage_in_memory import my_posts
from fastapi import APIRouter
router = APIRouter()

@router.get('/')
async def index(): 
    return my_posts