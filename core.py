import pyautogui
import time
from typing import Tuple

class MouseAutomationError(Exception):
    """Base class for mouse automation errors"""
    pass

class InvalidCoordinatesError(MouseAutomationError):
    """Raised when coordinates are invalid"""
    pass

class OutOfBoundsError(MouseAutomationError):
    """Raised when coordinates are outside screen bounds"""
    pass

class FailSafeTriggeredError(MouseAutomationError):
    """Raised when fail safe is triggered"""
    pass

def get_screen_dimensions() -> Tuple[int, int]:
    """Get current screen width and height"""
    try:
        width, height = pyautogui.size()
        if width <= 0 or height <= 0:
            raise MouseAutomationError("Invalid screen dimensions detected")
        return width, height

    except Exception as exc:
        raise MouseAutomationError(f"Failed to retrieve screen size: {exc}") from exc

def validate_click_position(x: int, y: int) -> None:
    """Validate click coordinates against edge cases"""
    if not isinstance(x, int) or not isinstance(y, int):
        raise InvalidCoordinatesError("X and Y must be integers")
    if x < 0 or y < 0:
        raise InvalidCoordinatesError("Coordinates cannot be negative")
    width, height = get_screen_dimensions()
    if x >= width or y >= height:
        raise OutOfBoundsError(f"Position ({x}, {y}) exceeds screen bounds ({width}, {height})")

def perform_click(x: int, y: int, num_clicks: int = 1, click_interval: float = 0.0) -> bool:
    """Execute click with comprehensive error handling"""
    try:
        validate_click_position(x, y)
        if num_clicks < 1:
            raise MouseAutomationError("Number of clicks must be positive")
        if click_interval < 0:
            raise MouseAutomationError("Click interval must be non-negative")
        pyautogui.click(x=x, y=y, clicks=num_clicks, interval=click_interval)
        return True

    except pyautogui.FailSafeException as exc:
        raise FailSafeTriggeredError("Fail-safe activated: mouse moved to corner") from exc
    except MouseAutomationError:
        raise
    except Exception as exc:
        raise MouseAutomationError(f"Unexpected click failure: {exc}") from exc

def run_autoclicker(x: int, y: int, total_duration: float = 10.0, interval_between_clicks: float = 0.05) -> None:
    """Run autoclicker loop handling various edge cases"""
    if total_duration <= 0:
        raise MouseAutomationError("Duration must be positive")
    start_time = time.time()
    try:
        while time.time() - start_time < total_duration:
            try:
                perform_click(x, y)
                time.sleep(interval_between_clicks)
            except (InvalidCoordinatesError, OutOfBoundsError, FailSafeTriggeredError) as err:
                print(f"Edge case encountered: {err}")
                break
            except MouseAutomationError as err:
                print(f"Automation error: {err}")
                break
    except KeyboardInterrupt:
        print("Autoclicker stopped by user interrupt")
    except Exception as err:
        print(f"Critical error in autoclicker: {err}")