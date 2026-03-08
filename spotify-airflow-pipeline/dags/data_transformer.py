import pandas as pd

def transform_playlist_data(df):
    """
    Performs data cleaning and transformations on the Spotify playlist dataset.
    """
    if df.empty:
        return df

    # 1. Remove duplicate tracks
    df = df.drop_duplicates(subset=["track_name", "artist_name"]).copy()

    # 2. Handle missing values (e.g., fill missing album names)
    df["album_name"] = df["album_name"].fillna("Unknown Album")

    # 3. Convert duration from milliseconds to minutes
    df["duration_min"] = (df["duration_ms"] / 60000).round(2)

    # 4. Extract release year from release date
    # Some dates are only YYYY, others are YYYY-MM-DD
    df["release_year"] = df["release_date"].apply(lambda x: x.split("-")[0] if isinstance(x, str) else None)

    # 5. Create popularity_category column
    def categorize_popularity(score):
        if score <= 40:
            return "Low"
        elif score <= 70:
            return "Medium"
        else:
            return "High"

    df["popularity_category"] = df["popularity"].apply(categorize_popularity)

    return df

def generate_summary_stats(df):
    """
    Calculates summary insights from the transformed data.
    """
    if df.empty:
        return "No data available."

    total_tracks = len(df)
    avg_duration = df["duration_min"].mean()
    top_artists = df["artist_name"].value_counts().head(5).to_dict()
    top_tracks = df.sort_values(by="popularity", ascending=False).head(5)[["track_name", "artist_name", "popularity"]].to_dict('records')

    summary = f"--- Spotify Playlist Summary ---\n"
    summary += f"Total Tracks: {total_tracks}\n"
    summary += f"Average Track Duration: {avg_duration:.2f} minutes\n\n"
    
    summary += "Top 5 Artists by Track Count:\n"
    for artist, count in top_artists.items():
        summary += f"- {artist}: {count} tracks\n"
    
    summary += "\nTop 5 Most Popular Tracks:\n"
    for track in top_tracks:
        summary += f"- {track['track_name']} by {track['artist_name']} (Popularity: {track['popularity']})\n"

    return summary
