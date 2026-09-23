from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings
#mongoclient = MongoClient(settings.MONGO_URI)
client : MongoClient = MongoClient(settings.MONGO_URI)
database : Database = client[settings.MONGO_DB_NAME]
# send a ping to confirm a successful connection
def ping_database() -> bool:
    try:
        client.admin.command('ping')
        return True
    except Exception:
        return False