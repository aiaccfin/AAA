import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI= os.getenv("MONGO_AIACCFIN")
print(MONGO_URI)

client = AsyncIOMotorClient(MONGO_URI)
db     = client.db_xai

users_collection  =  db.users
roles_collection  =  db.roles
groups_collection =  db.groups
biz_entities_collection = db.biz_entities

