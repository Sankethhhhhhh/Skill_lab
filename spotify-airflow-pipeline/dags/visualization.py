import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations(df):

    os.makedirs("/tmp/visuals", exist_ok=True)

    # Top artists
    top_artists = df["artist_name"].value_counts().head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=top_artists.values, y=top_artists.index)
    plt.title("Top Artists in Playlist")
    plt.tight_layout()

    plt.savefig("/tmp/visuals/artist_distribution.png")
    plt.close()


    # Popularity distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["popularity"], bins=20)
    plt.title("Track Popularity Distribution")
    plt.tight_layout()

    plt.savefig("/tmp/visuals/popularity_distribution.png")
    plt.close()


    # Mood distribution
    if "mood" in df.columns:

        plt.figure(figsize=(8,5))
        sns.countplot(x="mood", data=df)
        plt.title("Mood Distribution")
        plt.tight_layout()

        plt.savefig("/tmp/visuals/mood_analysis.png")
        plt.close()