import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Iniciando o rastreamento de tempo de execução da função: '{func.__name__}'")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = (end_time - start_time)
        print(f"O tempo total de execução da função '{func.__name__}' foi de: {total_time:.4f} segundos")
        return result
    return wrapper
        