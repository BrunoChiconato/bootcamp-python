import time
from log_execution_time import log_execution_time

@log_execution_time
def process_data():
    time.sleep(2)
    print("Dados processados")

def main():
    process_data()

if __name__ == '__main__':
    main()