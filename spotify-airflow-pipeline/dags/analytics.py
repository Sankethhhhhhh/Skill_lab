import pandas as pd

def run_analytics(df):
    """
    Performs deeper analytics on the transformed playlist data.
    """
    if df.empty:
        print("Analytics: No data to analyze.")
        return ""

    # Top 5 most popular tracks
    top_popular = df.sort_values(by='popularity', ascending=False).head(5)
    
    # Artist track counts
    artist_counts = df['artist_name'].value_counts()
    
    # Popularity stats
    pop_stats = df['popularity'].describe()
    
    # Mood distribution
    mood_dist = df['mood'].value_counts() if 'mood' in df.columns else "N/A"

    print("\n--- Advanced Analytics ---")
    print(f"Total Unique Artists: {len(artist_counts)}")
    print(f"Top Artist: {artist_counts.index[0]} ({artist_counts.iloc[0]} tracks)")
    print(f"Average Popularity: {pop_stats['mean']:.2f}")

    return {
        "top_popular": top_popular,
        "artist_counts": artist_counts,
        "pop_stats": pop_stats,
        "mood_dist": mood_dist
    }
