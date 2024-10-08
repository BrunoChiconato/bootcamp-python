from functools import wraps

def validate_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = args[0]

        if not isinstance(data, list):
            raise ValueError("O dado de entrada deve ser uma lista.")
        
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Cada item da lista deve ser um dicionário.")
            if not all(key in item for key in ['id', 'nome', 'idade']):
                raise ValueError("Cada dicionário deve conter as chaves 'id', 'nome' e 'idade'.")
        
        return func(*args, **kwargs)
    return wrapper
