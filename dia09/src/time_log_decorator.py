from loguru import logger #type: ignore
from functools import wraps
import time

logger.remove()
logger.add('./app.log', format="{time} {level} {message}", level="INFO")

def time_log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f'Chamando a função {func.__name__} com args:{args} e kwargs:{kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'A função {func.__name__} retornou: {result}')
            return result
        except Exception as e:
            logger.exception(f'Exceção capturada em {func.__name__}: {e}')
            raise
        finally:
            end_time = time.time()
            logger.info(f'Tempo de execução da função {func.__name__} foi: {(end_time - start_time):.3f} segundos')
    return wrapper