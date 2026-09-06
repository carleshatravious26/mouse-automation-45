import platform
from enum import Enum

# Cross-platform input definitions
SYSTEM_OS = platform.system()

class ClickType(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'
    DOUBLE = 'double'

class MouseAction(Enum):
    PRESS = 'press'
    RELEASE = 'release'
    CLICK = 'click'
    MOVE = 'move'

# Default application settings
DEFAULT_DELAY = 0.1
MAX_CLICK_RATE = 1000  # Clicks per second limit

# System specific modifiers
if SYSTEM_OS == "Darwin":
    COMMAND_KEY = "cmd"
else:
    COMMAND_KEY = "ctrl"

# Configuration constraints
MIN_X_COORD = 0
MIN_Y_COORD = 0
MAX_SCREEN_WIDTH = 1920
MAX_SCREEN_HEIGHT = 1080

def get_default_config():
    """Returns standard configuration dictionary."""
    return {
        "delay": DEFAULT_DELAY,
        "click_type": ClickType.LEFT.value,
        "is_enabled": False
    }