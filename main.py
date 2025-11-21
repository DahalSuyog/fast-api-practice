from fastapi import FastAPI, HTTPException


app = FastAPI()

items = ["apple", "banana", "cherry"]

@app.get("/")
def root():
    return {"message": "Hello, World"}

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items")
def read_limited_items(limit: int = 1):
    return items[:limit]


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id >= 0 and item_id < len(items):
        return { "item" : items[item_id]}
    else:
        raise HTTPException(status_code = 404, detail = "Item not found")
    
