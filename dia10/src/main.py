import time
import random
from log_execution_time import log_execution_time
from validate_data import validate_data
from limit_calls import limit_calls
from retry_on_failure import retry_on_failure
from cache_results import cache_results

@log_execution_time
def process_data():
    time.sleep(2)
    print("Dados processados")

@validate_data
def insert_data_in_database(data):
    print(f"Inserindo {len(data)} registro(s) no banco de dados")

@limit_calls(5)
def get_data_from_api():
    print("Fazendo requisição para a API")
    return {"data": "valor"}

@retry_on_failure
def fetch_data_from_database():
    if random.choice([True]):
        raise ConnectionError("Falha na conexão com o banco de dados")
    print("Dados obtidos com sucesso")

@cache_results
def heavy_computation(a, b):
    print(f"Processando dados com {a} e {b}...")
    time.sleep(1)
    return a + b

def main():
    a = 2
    b = 3
    for i in range(2):
        print(heavy_computation(a,b))

if __name__ == '__main__':
    main()