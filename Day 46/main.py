from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-modify-playback-state"

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
titles = [title.getText().strip() for title in soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")]
artists = [artist.getText().strip() for artist in soup.find_all(name="span", class_="a-no-trucate")]
# print(titles)
# print(artists)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

song_uris = []

for song in titles:
    artist = artists[titles.index(song)]
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]} artist:{artist}", type="track")
    try:
        sp.add_to_queue(uri=result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Could not find {song} - {artist}")



# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])