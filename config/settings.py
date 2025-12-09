# config/settings.py
import os
from dotenv import load_dotenv
from google.cloud import bigquery

# Carrega variáveis do .env
load_dotenv()

# -----------------------------
# TMDB
# -----------------------------
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_URL = "https://api.themoviedb.org/3/trending/movie/day"

if not TMDB_API_KEY:
    raise ValueError("TMDB_API_KEY não encontrado no .env")

# -----------------------------
# PostgreSQL
# -----------------------------
POSTGRES_URI = os.getenv("POSTGRES_URI")  # Ex: postgresql://postgres:senha@localhost:5432/tmdb_dw

if not POSTGRES_URI:
    raise ValueError("POSTGRES_URI não encontrado no .env")
else:
    print("POSTGRES_URI carregado com sucesso!")

# -----------------------------
# BigQuery
# -----------------------------
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BQ_DATASET = os.getenv("BQ_DATASET")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Verifica se o arquivo de credenciais existe
if not GOOGLE_APPLICATION_CREDENTIALS or not os.path.isfile(GOOGLE_APPLICATION_CREDENTIALS):
    raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {GOOGLE_APPLICATION_CREDENTIALS}")

# Define a variável de ambiente para autenticação
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# Inicializa o cliente BigQuery
bq_client = bigquery.Client(project=GCP_PROJECT_ID)

# Função opcional para testar conexão
def test_bigquery_connection():
    try:
        datasets = list(bq_client.list_datasets())
        print(f"✔ Conexão com BigQuery OK! Projeto: {bq_client.project}")
        if datasets:
            print("Datasets disponíveis:", [ds.dataset_id for ds in datasets])
        else:
            print("Nenhum dataset encontrado no projeto.")
    except Exception as e:
        print("✘ Erro ao conectar com BigQuery:", e)

# Testa conexão automaticamente ao importar (opcional)
if __name__ == "__main__":
    test_bigquery_connection()
