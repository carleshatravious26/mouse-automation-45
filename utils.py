import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("mouse_automation.utils")

def retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function call if specific exceptions are raised.

    :param retries: Number of times to retry before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    :param exceptions: Tuple of exception classes that trigger a retry.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(
                            f"Failed {func.__name__} after {retries} attempts. Error: {e}"
                        )
                        raise e
                    
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}. "
                        f"Retrying in {current_delay:.1f} seconds... Error: {e}"
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator