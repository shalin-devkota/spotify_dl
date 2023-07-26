from .client import spotify
from .dbhandler import get_tracked_playlists, get_last_snapshot, get_last_length

"""
Future change: CAll spotify once, store it globally and derive from there rather than multiple calls.
"""


def find_changes(id):
    last_length = get_last_length(id)
    cur_length = len(spotify.playlist(id)["tracks"]["items"])
    print(last_length, cur_length)


def sync_playlist():
    tracked_playlists = get_tracked_playlists()
    i = 1
    for key in tracked_playlists.keys():
        print(f"{i}. {key}")
        i += 1
    choice = int(input("Enter the playlist you would like to track: "))
    playlist_id = list(tracked_playlists.keys())[choice - 1]
    playlist_id = tracked_playlists[playlist_id]
    last_snapshot = get_last_snapshot(playlist_id)
    cur_snapshot = spotify.playlist(playlist_id)["snapshot_id"]
    if cur_snapshot == last_snapshot:
        print("The playlist is already synced.")
    else:
        print("Changes detected.")
        find_changes(playlist_id)
