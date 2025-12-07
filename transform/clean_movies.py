import pandas as pd

def normalize_movies(raw_data):
    df = pd.json_normalize(raw_data)

    # Selecionar apenas colunas úteis
    df = df[[
        'id', 'title', 'original_language', 'release_date',
        'vote_average', 'vote_count', 'popularity'
    ]]

    df['release_date'] = pd.to_datetime(df['release_date'], errors="coerce")

    return df