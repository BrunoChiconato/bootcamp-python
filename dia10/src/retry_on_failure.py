from functools import wraps
import time 

def retry_on_failure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Tentativa {attempt} falhou com erro: {e}")
                if attempt == max_retries:
                    print("Máximo de tentativas atingido, propagando a exceção.")
                    raise
                else:
                    print("Tentando novamente...")
                    time.sleep(1)
    return wrapper
