from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#pip install fastapi uvicorn
#uvicorn main:app --reload



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "First Item", "description": "This is the first time."}

