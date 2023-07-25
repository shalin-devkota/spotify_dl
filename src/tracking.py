from client import spotify
from dbhandler import add_to_db


def track(playlist_url):
    playlist = spotify.playlist(playlist_url)
    playlist_id = playlist["id"]
    playlist_name = playlist["name"]
    snapshot = playlist["snapshot_id"]
    add_to_db(playlist_id, playlist_name, snapshot)


track("https://open.spotify.com/playlist/46jC89e0qdF2FQnTin1VTj?si=e3f557a296154af0")
