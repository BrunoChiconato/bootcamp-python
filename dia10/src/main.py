import time
from log_execution_time import log_execution_time
from validate_data import validate_data
from limit_calls import limit_calls

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

def main():
    for _ in range(6):
        try:
            get_data_from_api()
        except RuntimeError as e:
            print(e)
if __name__ == '__main__':
    main()