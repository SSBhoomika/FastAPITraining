#this is the main entry point of the application. 
from fastapi import FastAPI
from app.config import settings
from app.database import ping_database

app = FastAPI(title=settings.APP_NAME)
#this function runs when the application starts up. It checks if the database is connected

@app.on_event("startup")
def on_startup():
    if not ping_database():
        raise RuntimeError("Could not connect to the MongoDB")
    print(f"[startup]Connected to the MongoDB. App:{settings.APP_NAME}")

@app.get("/",tags=["Health"])
def health_check():
    return {"status": "ok", "app_name": settings.APP_NAME}