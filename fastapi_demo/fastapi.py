#!d:\cccc2020\TOOL\python-3.9.1-embed-win32\python.exe
from typing import Optional

from fastapi import FastAPI


#uvicorn test:app --reload

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

