"""Constants and limits for the mouse-automation-45 autoclicker."""

from typing import Tuple

# Speed limits to prevent system instability or application crashes
MIN_CLICK_DELAY_SECS: float = 0.001  # Maximum 1000 clicks per second
MAX_CLICK_DELAY_SECS: float = 3600.0  # 1 hour maximum interval
DEFAULT_CLICK_DELAY_SECS: float = 0.1

# Coordinate bounds based on screen dimensions or generic safe limits
MIN_SCREEN_COORDINATE: int = 0
MAX_SCREEN_COORDINATE_X: int = 7680  # Support up to 8K width
MAX_SCREEN_COORDINATE_Y: int = 4320  # Support up to 8K height

# Safety emergency stop configuration (fail-safe trigger)
DEFAULT_FAILSAFE_KEY: str = "esc"
FAILSAFE_CORNER: Tuple[int, int] = (0, 0)

# Mouse buttons mapping
ALLOWED_MOUSE_BUTTONS: Tuple[str, ...] = ("left", "right", "middle")

# Error message templates for edge case handling
ERROR_INVALID_DELAY: str = f"Delay must be between {MIN_CLICK_DELAY_SECS} and {MAX_CLICK_DELAY_SECS} seconds."
ERROR_OUT_OF_BOUNDS: str = "Coordinates must be within the detectable screen area."
ERROR_INVALID_BUTTON: str = f"Button must be one of: {', '.join(ALLOWED_MOUSE_BUTTONS)}"
ERROR_FAILSAFE_TRIGGERED: str = "Failsafe triggered by moving the mouse to the corner or pressing the stop key."
