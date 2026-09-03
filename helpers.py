import logging
import pyautogui
from typing import Tuple, Optional

logger = logging.getLogger('mouse-automation-45')

def validate_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Ensures mouse coordinates are within screen boundaries."""
    try:
        screen_width, screen_height = pyautogui.size()
        safe_x = max(0, min(x, screen_width))
        safe_y = max(0, min(y, screen_height))
        return safe_x, safe_y
    except Exception as e:
        logger.error(f"Failed to validate coordinates: {e}")
        return 0, 0

def safe_click(x: int, y: int, interval: float = 0.1) -> bool:
    """Attempts a mouse click with fail-safe boundaries."""
    try:
        target_x, target_y = validate_coordinates(x, y)
        pyautogui.click(target_x, target_y)
        return True
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user")
        return False
    except Exception as e:
        logger.error(f"Click action failed at ({x}, {y}): {e}")
        return False

def get_screen_dimensions() -> Tuple[int, int]:
    """Retrieves display resolution with error recovery."""
    try:
        return pyautogui.size()
    except Exception:
        return 1920, 1080