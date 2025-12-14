from extract.fetch_api import fetch_trending_movies
from transform.clean_movies import normalize_movies
from load.load_dw import load_to_postgres, load_to_bigquery

def run_pipeline():
    print("Extraindo dados...")
    raw = fetch_trending_movies()

    print("Transformando...")
    df = normalize_movies(raw)

    print("Carregando no PostgreSQL (Data Warehouse local)...")
    load_to_postgres(df)

    print("Carregando no BigQuery (Data Warehouse nuvem)...")
    load_to_bigquery(df)

    print("Pipeline finalizada!")

if __name__ == "__main__":
    run_pipeline()