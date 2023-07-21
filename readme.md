# Spotify Downloader

## Requirements

- Python 3.10+
- [Pytube](https://pytube.io/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)

## Setup Spotipy

To use Spotipy, you need to install it and follow the instructions from the [official documentation](https://spotipy.readthedocs.io/en/2.22.1/) to set it up properly.

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Patching pytube files

Pytube's default client is set to `ANDROID_MUSIC` which marks some videos as falsely age restricted. To fix this, navigate to
`pytube` -> `contrib`-> `innerTube`. Inside the `__init__` method of the InnerTube class, change the client to `WEB`.

## Usage

1. Run the extractor.py file
2. Paste the URL of the playlist you wish to download
3. The songs will be downloaded inside downloads/name_of_your_playlist

## Limitations

1. Your liked songs play list cannot be downloaded.
2. The songs are searched for in youtube. Age restricted videos cannot be downloaded (unless you add Oauth).

## Adding Ouath

In `downloader.py` modify

```python
song = YouTube(a)
```

to

```python
song= Youtube(a,use_oauth=True,allow_oauth_cache=False)

```

##
