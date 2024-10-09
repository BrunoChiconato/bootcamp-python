from functools import wraps

def limit_calls(num_requisicoes: int):
    def decorator(func):
        contador = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal contador

            if contador == num_requisicoes:
                raise RuntimeError("Você atingiu o limite de chamadas da função!")

            result = func(*args,**kwargs)
            contador += 1
            
            return result
        return wrapper
    return decorator