import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    """Centralized configuration and environment variable management."""
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI', 'http://127.0.0.1:8888/callback')
    PLAYLIST_ID = os.getenv('PLAYLIST_ID')


    @classmethod
    def validate(cls):
        """Validate that required environment variables are set."""
        required = ['SPOTIPY_CLIENT_ID', 'SPOTIPY_CLIENT_SECRET', 'PLAYLIST_ID']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")
        return True
