import os
from downloader import download_handler
from client import spotify

songs = []


def get_song_list(url):
    play_list_name = spotify.playlist(url)["name"]
    result = spotify.playlist_tracks(url)

    play_list_length = len(result["items"])

    for i in range(play_list_length):
        song_name = result["items"][i]["track"]["name"]
        artist_name = result["items"][i]["track"]["album"]["artists"][0]["name"]
        if song_name != "":
            songs.append(f"{song_name} - {artist_name}")

    download_handler(songs, play_list_name)


url = input("Enter the playlist URL: ")
get_song_list(url)

"""
There is no need to call spotify 2 times as both the tracks and playlist name can be obtained through a  single method.
Only realised it after I wrote code to extract names! Change this in the future! 
"""

if __name__ == "__main__":
    get_song_list()
