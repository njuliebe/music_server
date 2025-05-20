from fastapi import FastAPI
from music_get import fangpi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/music/search")
def get_music(keyword: str, proxy: bool):
    return fangpi.get_music_info(keyword, proxy)