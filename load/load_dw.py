from sqlalchemy import create_engine
from config.settings import POSTGRES_URI, GCP_PROJECT_ID, BQ_DATASET
from pandas_gbq import to_gbq

# Função para carregar no PostgreSQL
def load_to_postgres(df, table_name="movies"):
    engine = create_engine(POSTGRES_URI)
    df.to_sql(table_name, engine, if_exists="append", index=False) # append/replace
    print(f"✔ Tabela {table_name} carregada no PostgreSQL com sucesso!")

# Função para carregar no BigQuery
def load_to_bigquery(df, table_name="movies"):
    # Nome completo da tabela no BigQuery: dataset.tabela
    table_id = f"{BQ_DATASET}.{table_name}"

    # Carrega DataFrame para BigQuery
    to_gbq(
        dataframe=df,
        destination_table=table_id,
        project_id=GCP_PROJECT_ID,
        if_exists="append") # append/replace
    print(f"✔ Tabela {table_name} carregada no BigQuery com sucesso!")