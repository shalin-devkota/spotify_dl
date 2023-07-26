from .client import spotify
from .dbhandler import get_tracked_playlists, get_last_snapshot


def sync_playlist():
    tracked_playlists = get_tracked_playlists()
    i = 1
    for key in tracked_playlists.keys():
        print(f"{i}. key")
        i += 1
    choice = input("Enter the playlist you would like to track: ")
    # last_snapshot = get_last_snapshot()
    print(choice)


sync_playlist()
