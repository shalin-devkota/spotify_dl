import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from downloader import download_handler

os.environ["SPOTIPY_CLIENT_ID"] = "6e4ea7528d414ce398f1b8b66b3d54ff"
os.environ["SPOTIPY_CLIENT_SECRET"] = "3f753de9e2b742a2b8ee0c2bd300ecde"

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
