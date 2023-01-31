from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def home():
    return {"message":"hello!"}

@app.get("/search")
def search(query: str):
    return {"message": f"You searched for: {query}"}