import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from downloader import download_handler
from dotenv import load_dotenv


load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
songs = []


def get_song_list(url):
    result = spotify.playlist_tracks(url)

    play_list_length = len(result["items"])

    for i in range(play_list_length):
        song_name = result["items"][i]["track"]["name"]
        artist_name = result["items"][i]["track"]["album"]["artists"][0]["name"]
        if song_name != "":
            songs.append(f"{song_name} - {artist_name}")


url = input("Enter the playlist URL: ")

"""
There is no need to call spotify 2 times as both the tracks and playlist name can be obtained through a  single method.
Only realised it after I wrote code to extract names! Change this in the future! 
"""

play_list_name = spotify.playlist(url)["name"]
get_song_list(url)
download_handler(songs, play_list_name)
