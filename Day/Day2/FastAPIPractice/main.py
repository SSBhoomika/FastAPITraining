from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"page": "home"}
@app.get("/about")
def read_about():   
    return {"page": "about","author": "Bhoomika"}
@app.get("/health")
def read_health():
    return {"status": "healthy"}    
