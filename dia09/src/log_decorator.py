from loguru import logger #type: ignore
from functools import wraps

logger.remove()
logger.add('./app.log', format="{time} {level} {message} {file}", level="INFO")

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Chamando a função {func.__name__} com args:{args} e kwargs:{kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'A função {func.__name__} retornou: {result}')
            return result
        except Exception as e:
            logger.exception(f'Exceção capturada em {func.__name__}: {e}')
            raise
    return wrapper