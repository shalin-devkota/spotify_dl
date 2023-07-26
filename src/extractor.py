from .downloader import download_handler
from .client import spotify

songs = []


def get_song_list(url=None):
    if url is None:
        url = input("Enter the playlist url you would like to download: ")
    play_list_name = spotify.playlist(url)["name"]
    result = spotify.playlist_tracks(url)

    play_list_length = len(result["items"])

    for i in range(play_list_length):
        song_name = result["items"][i]["track"]["name"]
        artist_name = result["items"][i]["track"]["album"]["artists"][0]["name"]
        if song_name != "":
            songs.append(f"{song_name} - {artist_name}")

    download_handler(songs, play_list_name)


if __name__ == "__main__":
    get_song_list()
