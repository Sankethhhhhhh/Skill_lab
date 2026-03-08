def classify_mood(df):
    """
    Simulates mood classification based on track popularity and duration.
    In a real scenario, this would use audio features like valence and energy.
    """
    if df.empty:
        return df

    def get_mood(row):
        # A simple rule-based mood classification for demonstration
        pop = row.get('popularity', 0)
        dur = row.get('duration_ms', 0)
        
        if pop > 75:
            return "Energetic"
        elif pop > 50:
            return "Happy"
        elif dur > 240000: # > 4 mins
            return "Chill"
        else:
            return "Sad"

    df['mood'] = df.apply(get_mood, axis=1)
    return df
