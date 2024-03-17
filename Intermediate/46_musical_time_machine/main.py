import requests
import spotipy

from bs4 import BeautifulSoup
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

when = "2003-09-01"#input("Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")

def get_songs(date):
    url = f'https://www.billboard.com/charts/hot-100/{when}/'

    response = requests.get(url=url)

    soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('li ul li h3')
    
    return [song.getText().strip() for song in songs]

songs_titles = get_songs(when)
print("Songs collected.")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private', 
        show_dialog=True, 
        cache_path='token.txt'
        )
)

user_id = sp.current_user()["id"]

songs_uris = []

for song in songs_titles:
    result = sp.search(q=song, type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uris.append(uri)
        
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
print("URI collected too")

playlist = sp.user_playlist_create(
    user=user_id, 
    name=f"{when} Billboard 100",
    public=False,
)
print("Playlist created")

sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=songs_uris,
)
print("Songs added.")