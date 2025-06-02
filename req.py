import requests

def get_music_info():
    url = 'http://127.0.0.1:8000/music/search'
    headers = {
        'Authorization': 'Bearer 123567'
    }
    resp = requests.post(url, json={
        'keyword': '稻香',
        'proxy': False
    }, headers=headers)
    print(resp.json())

if __name__ == "__main__":
    get_music_info()
