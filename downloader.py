import os
from pytube import Search, YouTube
import json
import re

if not os.path.exists("downloads"):
    os.makedirs("downloads")


def download_handler(songs, play_list_name):
    skipped_songs = []
    if not os.path.exists(f"downloads/{play_list_name}"):
        os.makedirs(f"downloads/{play_list_name}")

    for song in songs:
        search_results = Search(song)
        for result in search_results.results:
            a = result.watch_url
            break
        song_name = song
        song = YouTube(
            a,
        )

        try:
            audio_stream = song.streams.filter(only_audio=True).first()
            print("Downloading... ")
            format_song_name = lambda song_name: re.sub(r"[^\w\s-]", "", song_name)
            song_name = format_song_name(song_name)
            audio_stream.download(
                output_path=f"downloads/{play_list_name}", filename=f"{song_name}.mp4"
            )
            print(f"Downloaded {song.title}")
        except Exception as e:
            print(e)
            print("Some error occurred. Skipping current song")
            skipped_songs.append(song)
            continue
    print("Downloads finished. Following songs were skipped.")
    for song in skipped_songs:
        print(song.title)


# print(f"Downloading {video.title}")
# video_stream = video.streams.get_audio_only()

# video_stream.download()

if __name__ == "__main__":
    download_handler()
