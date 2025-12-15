#from fastapi import FastAPI, HTTPException, UploadFile, File
#from pydantic import BaseModel



#app = FastAPI()

'''
items = []

class Item(BaseModel):
    name: str 
    is_available: bool = True


@app.get("/")
def root():
    return {"message": "Hello, World", "status": "success"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items")
def read_limited_items(limit: int = 1):
    return items[:limit]


@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
    if item_id >= 0 and item_id < len(items):
        return { "item" : items[item_id]}
    else:
        raise HTTPException(status_code = 404, detail = "Item not found")
    
#front to docs send pdf/txt file save to local system and read from local system according flietype
# chunk the files using 2 strategy 
'''
'''
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), name: str = Form(...), chunk_size: int = Form(0), total_chunks: int = Form(0)):
    content = await file.read()
    #processing file content
    from fastapi import FastAPI
from database import engine, Base
from routers import ingestion
'''

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Document Ingestion API")

app.include_router(ingestion.router, prefix="/api/v1", tags=["Ingestion"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)