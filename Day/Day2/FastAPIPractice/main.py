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
@app.get("/create")
def read_create():
    return {"page": "create"}

#path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn": usn} 
@app.get("/student/{rollno}")
def get_result(rollno:int):
    return {"Result":"Distinction","rollno": rollno} 
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
@app.post("/items")
def create_item(item: Item):
    return{"recieved_item": item,"total_price": item.price * 1.18}