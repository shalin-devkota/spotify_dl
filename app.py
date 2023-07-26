from src.extractor import get_song_list
from src.tracking import track
from src.sync import sync_playlist

print("Welcome to spotify syncer")

print("1. Download a playlist")
print("2. Start tracking a playlist")
print("3. Sync a playlist")

choice = int(input("Enter you choice: "))

if choice == 1:
    get_song_list()
elif choice == 2:
    track()
elif choice == 3:
    sync_playlist()

else:
    print("Invalid choice!")
