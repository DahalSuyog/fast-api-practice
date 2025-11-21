from fastapi import FastAPI


app = FastAPI()

items = ["apple", "banana", "cherry"]

@app.get("/")
def root():
    return {"message": "Hello, World"}

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items[item_id]
    return item
