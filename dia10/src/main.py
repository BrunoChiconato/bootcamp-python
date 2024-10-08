import time
from log_execution_time import log_execution_time
from validate_data import validate_data

@log_execution_time
def process_data():
    time.sleep(2)
    print("Dados processados")

@validate_data
def insert_data_in_database(data):
    print(f"Inserindo {len(data)} registro(s) no banco de dados")

def main():
    data = [{"id": 1, "nome": "asd", "IDADE": 23}]
    insert_data_in_database(data)

if __name__ == '__main__':
    main()