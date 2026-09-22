from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World","Message": "Welcome to the FastAPI app"}
