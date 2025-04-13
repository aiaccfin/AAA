import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI= os.getenv("MONGO_AIACCFIN")

client = AsyncIOMotorClient(MONGO_URI)
db     = client.db_xai

users_collection  =  db.users
roles_collection  =  db.roles
groups_collection =  db.groups
invoice_collection =  db.invoices

biz_entities_collection = db.biz_entities
verification_collection = db.verification_collection

