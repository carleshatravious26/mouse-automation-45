import sys
from typing import Final

# performance settings for high-frequency input simulation
DEFAULT_CLICK_INTERVAL: Final[float] = 0.001
MAX_CLICK_RATE: Final[int] = 1000

# buffer sizing for mouse event queueing
EVENT_BUFFER_SIZE: Final[int] = 2048

# thread priority and optimization flags
ENABLE_GIL_RELEASE: Final[bool] = True
USE_FAST_PATH: Final[bool] = sys.platform.startswith('win')

# resource management constants
MAX_WORKER_THREADS: Final[int] = 4
IDLE_POLL_RATE: Final[float] = 0.016

# system coordinate constraints
SCREEN_MIN_WIDTH: Final[int] = 0
SCREEN_MIN_HEIGHT: Final[int] = 0

def get_performance_mode() -> dict:
    """returns dict of hardware-specific performance settings."""
    return {
        "buffer": EVENT_BUFFER_SIZE,
        "fast_path": USE_FAST_PATH,
        "threads": MAX_WORKER_THREADS
    }