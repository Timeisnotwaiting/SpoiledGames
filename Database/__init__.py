from config import DB_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(DB_URL)

db = mongo.SPL



