from src.extractor import get_song_list
from src.tracking import track

print("Welcome to spotify syncer")

print("1. Download a playlist")
print("2. Start tracking a playlist")

choice = int(input("Enter you choice: "))

if choice == 1:
    get_song_list()
if choice == 2:
    track()
else:
    print("Invalid choice!")
