from .client import spotify
from .dbhandler import add_to_db


def track(playlist_url=None):
    if playlist_url is None:
        playlist_url = input("Enter the playlist url you wish to track: ")

    playlist = spotify.playlist(playlist_url)
    number_of_tracks = len(playlist["tracks"]["items"])
    print(number_of_tracks)
    playlist_id = playlist["id"]
    playlist_name = playlist["name"]
    snapshot = playlist["snapshot_id"]

    add_to_db(playlist_id, playlist_name, snapshot, number_of_tracks)
