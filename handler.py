import logging
import pyautogui
import sys

logger = logging.getLogger(__name__)

def safe_mouse_click(x, y):
    """Executes a mouse click with fail-safe checks."""
    try:
        # Ensure coordinates are within screen bounds
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")

        # Fail-safe: moving mouse to 0,0 aborts execution
        pyautogui.FAILSAFE = True
        pyautogui.click(x, y)
        return True

    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered: mouse moved to corner")
        sys.exit(1)
    except pyautogui.PyAutoGUIException as e:
        logger.error(f"PyAutoGUI internal error: {e}")
        return False
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error during click: {e}")
        return False

def validate_coordinates(coords):
    """Validates input tuple for mouse interaction."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        return False
    return all(isinstance(i, (int, float)) for i in coords)