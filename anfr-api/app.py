from typing import Union
from fastapi import FastAPI
from database import SessionLocal
from import_service import ImportService

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

database = get_db()

importService = ImportService(database)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/import")
def importDB():
    return importService.importAntenna()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
