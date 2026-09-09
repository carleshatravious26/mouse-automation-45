import pyautogui
import time
import logging

class ClickHandler:
    """Handles mouse click execution and interval timing."""
    
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.logger = logging.getLogger(__name__)

    def perform_click(self, x: int, y: int) -> None:
        """Executes a single click at coordinates and enforces interval."""
        try:
            pyautogui.click(x=x, y=y)
            time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Click failure at ({x}, {y}): {e}")

    def run_sequence(self, coordinates: list) -> None:
        """Iterates through provided coordinate list."""
        for x, y in coordinates:
            self.perform_click(x, y)

class ClickConfiguration:
    """Encapsulates runtime parameters."""
    
    @staticmethod
    def validate_interval(interval: float) -> float:
        """Ensures interval is within safe performance bounds."""
        return max(0.01, min(interval, 5.0))