import requests
from config.settings import TMDB_API_KEY, TMDB_URL

def fetch_trending_movies():
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(TMDB_URL, params=params)
    response.raise_for_status()
    return response.json()["results"]