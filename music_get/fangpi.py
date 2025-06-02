from bs4 import BeautifulSoup
import requests
import json

def get_music_info(keyword, proxy=False):
    encodeKeyword = requests.utils.quote(keyword)
    
    if proxy:
        requests.proxies = {
            "http": "http://127.0.0.1:1087"
        }
    resp = requests.get(f"https://www.fangpi.net/s/{encodeKeyword}", verify=False)
    soup = BeautifulSoup(resp.content,"html.parser")
    cards = soup.find_all('div', class_='card mb-1')

    rows = []
    if cards: 
        rows = cards[0].find_all('div', class_='col-8 col-content') 
        

    list =[]
    for row in rows: 
        a_tag = row.find('a', class_='music-link')
        if a_tag:
            href = a_tag['href']
            title = a_tag.find('span', class_='music-title').text.strip()
            artist = a_tag.find('small', class_='text-jade').text.strip()
            play_id = get_music_play_id(href)
            play_url = None
            if play_id:
                play_url = get_music_play_url(play_id)
            list.append({
                'id': href.split('/')[-1],
                'title': title,
                'artist': artist,
                'href': href,
                'play_url': play_url
            })
    return list

def get_music_play_id(href):
    url = 'https://www.fangpi.net' + href
    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.content, "html.parser")
    script = soup.find('script', type='text/javascript')
    if script:
        import re
        match = re.search(r'"play_id"\s*:\s*"([^"]+)"', script.string)
        if match:
            return match.group(1)
    return None

def get_music_play_url(play_id):
    url = 'https://www.fangpi.net/api/play-url'
    body = {
        "id": play_id,
    }
    resp = requests.post(url, json=body, verify=False)
    # print(resp.json())
    if resp.status_code == 200:
        data = resp.json()
        if data['code'] == 1:
            play_url = data['data']['url']
            return play_url
        else:
            return None

if __name__ == "__main__":
    keyword = "稻香"
    resp = get_music_info(keyword, False)

    print(json.dumps(resp))