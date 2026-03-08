import pandas as pd
import requests


DATA_URL = "https://raw.githubusercontent.com/rushi4git/spotify-playlist-data/refs/heads/main/spotify_playlist.json"


def fetch_playlist_data():
    """
    Fetch playlist data from provided JSON dataset
    and convert it into a pandas DataFrame
    """

    print("Fetching playlist data from JSON dataset...")

    response = requests.get(DATA_URL)
    response.raise_for_status()

    data = response.json()

    tracks = []

    for track in data["tracks"]:

        tracks.append({
            "playlist_name": data.get("name", "spotify_playlist"),
            "track_id": track.get("track_id"),
            "track_name": track.get("track_name"),
            "artist_name": track.get("artist_name"),
            "album_name": track.get("album_name"),
            "popularity": track.get("popularity"),
            "duration_ms": track.get("duration_ms"),
            "release_date": track.get("release_date")
        })

    df = pd.DataFrame(tracks)

    print(f"Fetched {len(df)} tracks")

    return df