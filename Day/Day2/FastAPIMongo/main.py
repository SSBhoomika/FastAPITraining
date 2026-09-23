from fastapi import FastAPI
from pymongo import AsyncMongoClient
app = FastAPI()
client = AsyncMongoClient("mongodb://localhost:27017/")
db = client["college"]
collection = db["student"]
@app.get("/")
async def read_root():
    return {"page": "home"}
@app.get("/health")
async def read_health():
    result = await db.command("ping")
    if result["ok"] == 1.0:
        return {"mongo_status": "connected","ping_result": result["ok"]}