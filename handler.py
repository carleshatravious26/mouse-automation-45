import time
import requests
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_attempts=3, delay=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

@retry_network_op(max_attempts=3)
def fetch_remote_config(url):
    """Fetches remote configuration with retry capability."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()