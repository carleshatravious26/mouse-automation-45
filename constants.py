import sys
from typing import Final

# Application Metadata
APP_NAME: Final[str] = "MouseAutomation45"
APP_VERSION: Final[str] = "1.2.0"

# Default Click Configurations
DEFAULT_CLICK_INTERVAL: Final[float] = 0.1  # Seconds between clicks
DEFAULT_CLICK_BUTTON: Final[str] = "left"   # 'left', 'right', or 'middle'
DEFAULT_CLICK_TYPE: Final[str] = "single"   # 'single', 'double', or 'hold'

# Safety and Boundary Limits
MIN_INTERVAL_SECONDS: Final[float] = 0.001
MAX_INTERVAL_SECONDS: Final[float] = 3600.0
FAILSAFE_CORNER_SIZE: Final[int] = 10       # Pixels from screen corner to trigger failsafe

# Hotkey Binding Defaults
DEFAULT_START_HOTKEY: Final[str] = "<f8>"
DEFAULT_STOP_HOTKEY: Final[str] = "<f9>"
DEFAULT_TOGGLE_HOTKEY: Final[str] = "<f6>"

# Platform Specifics
IS_WINDOWS: Final[bool] = sys.platform == "win32"
IS_MACOS: Final[bool] = sys.platform == "darwin"
IS_LINUX: Final[bool] = sys.platform.startswith("linux")
