from functools import wraps

def cache_results(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        
        if key in cache:
            print("Retornando resultado do cache...")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper
