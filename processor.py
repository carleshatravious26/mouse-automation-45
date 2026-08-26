import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('mouse-automation-45')

class ClickProcessor:
    """Processes click sequences with safety boundaries and error handling."""
    
    def __init__(self, max_cps: int = 50):
        self.max_cps = max_cps
        self.min_interval = 1.0 / max_cps if max_cps > 0 else 0.02

    def validate_coordinates(self, x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
        """Ensure coordinates stay within physical screen bounds to prevent off-screen anomalies."""
        try:
            safe_x = max(0, min(x, screen_width))
            safe_y = max(0, min(y, screen_height))
            return safe_x, safe_y
        except Exception as e:
            logger.error(f"Coordinate validation failed: {e}")
            return 0, 0

    def process_click_delay(self, interval: float) -> float:
        """Throttle interval to prevent exceeding maximum CPS limits."""
        if interval < 0:
            logger.warning("Negative interval detected, resetting to minimum safe delay.")
            return self.min_interval
            
        if interval < self.min_interval:
            return self.min_interval
            
        return interval

    def execute_action(self, action_func, *args, **kwargs):
        """Safely execute a click action with exception suppression and logging."""
        try:
            return action_func(*args, **kwargs)
        except ZeroDivisionError:
            logger.error("Division by zero encountered during timing calculation.")
            return None
        except Exception as e:
            logger.critical(f"Unexpected error during click execution: {e}")
            return None
