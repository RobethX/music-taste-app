VERBOSE = True
DEBUG = True

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), verbose=VERBOSE)

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")
LASTFM_API_KEY=os.getenv("LASTFM_API_KEY")
LASTFM_SHARED_SECRET=os.getenv("LASTFM_SHARED_SECRET")