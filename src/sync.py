from client import spotify
from dbhandler import get_tracked_playlists


def sync_playlist(playlist_id):
    tracked_playlists = get_tracked_playlists()
    print("Please select a playlist to sync from")
    playlists = get_tracked_playlists()
    i = 1
    for playlist in playlists:
        print(f"{i}. {playlist}")
        i += 1
    choice = input("Enter your choice: ")


sync_playlist(1)
