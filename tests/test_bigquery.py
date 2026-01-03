from google.cloud import bigquery
import os

# Define o caminho do JSON da Service Account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Brian/Documents/Visual Studio Code/data engineer/etl_tmdb_dw/credentials/projetos-de-teste-445920-0c555f185dc7.json"

try:
    client = bigquery.Client()
    print("✔ Conexão com BigQuery OK! Projeto:", client.project)

    # Listar datasets do projeto
    datasets = list(client.list_datasets())
    if datasets:
        print("Datasets disponíveis:")
        for ds in datasets:
            print("-", ds.dataset_id)
    else:
        print("Nenhum dataset encontrado no projeto.")

except Exception as e:
    print("✘ Erro ao conectar com BigQuery:", e)