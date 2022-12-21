from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import dotenv

hidden_file = dotenv.find_dotenv()
dotenv.load_dotenv(hidden_file)

spotify_client_id = os.environ.get("CLIENT_ID")
spotify_client_secret = os.getenv("CLIENT_SECRET")
spotify_redirect_uri = os.environ.get("REDIRECT_URI")

year_to_travel = input("What year do you want to travel to? Type the date in YYYY-MM-DD: ")
year = year_to_travel.split("-")[0]
songs_response = requests.get(f"https://www.billboard.com/charts/hot-100/{year_to_travel}")
songs_response.raise_for_status()
song_billboard = songs_response.text
soup = BeautifulSoup(song_billboard, "html.parser")
songs_list = [song.get_text().strip("\n\t") for song in soup.find_all(name="h3", class_="a-no-trucate")]
artists = [artist.get_text().strip("\n\t") for artist in soup.find_all(name="span", class_="a-no-trucate")]


spot = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="2fe62023eaf24106a5b0e98bb0b83ed9",
                                                 client_secret="25c9d4ed77164320923ae0e81a72426e",
                                                 redirect_uri="http://example.com", state=None,
                                                 scope="playlist-modify-private", cache_path=None, username=None,
                                                 proxies=None, show_dialog=False, requests_session=True,
                                                 requests_timeout=50))
user_id = spot.me()["id"]
spotify_uris = []
for song_title in songs_list:
    try:
        search_results = spot.search(q=f"track:{song_title} year:{year}", type="track")
        spotify_uris.append(search_results["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")

empty_playlist = spot.user_playlist_create(user=user_id, name=f"{year_to_travel} Billboard 100", public=False,
                                           collaborative=False, description=f"Obiora's {year} Spotify Playlist")
playlist_id = empty_playlist["id"]
playlist = spot.playlist_add_items(playlist_id=playlist_id, items=spotify_uris)
