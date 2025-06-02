import yaml
import uvicorn
from fastapi import FastAPI, Header
from music_get import fangpi


app = FastAPI()


with open('config.yaml') as f:
    config = yaml.safe_load(f)
STATIC_TOKEN = config['token']

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/music/search")
def get_music(body: dict, authorization: str = Header(None)):
    if authorization != f"Bearer {STATIC_TOKEN}":
        return {"error": "Unauthorized"}
    keyword = body.get('keyword', '')
    proxy = body.get('proxy', False)
    return fangpi.get_music_info(keyword, proxy)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)