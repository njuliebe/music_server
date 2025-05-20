from fastapi import FastAPI
from music_get import fangpi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/music/{item_keyword}")
def get_music(item_keyword: str):
    return fangpi.get_music_info(item_keyword)