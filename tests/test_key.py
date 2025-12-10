import os
import requests
from dotenv import load_dotenv

load_dotenv()  # se estiver usando .env

API_KEY = os.getenv("TMDB_API_KEY")
URL = "https://api.themoviedb.org/3/trending/movie/day"

params = {"api_key": API_KEY}

response = requests.get(URL, params=params)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("✔ Chave funcionando!")
    print("Primeiro resultado:", response.json()["results"][0]["title"])
else:
    print("✘ Erro:", response.json())