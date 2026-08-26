import pyautogui
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MouseClickHandler:
    # Initialize with failsafe and screen dimensions
    def __init__(self):
        pyautogui.FAILSAFE = True
        try:
            self.screen_width, self.screen_height = pyautogui.size()
        except Exception:
            self.screen_width, self.screen_height = 1920, 1080
            logging.warning("Using default screen size")

    # Validate click position against screen bounds
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x > self.screen_width or y > self.screen_height:
            logging.error("Coordinates outside screen bounds")
            return False
        return True

    # Perform click with checks for invalid parameters and exceptions
    def safe_click(self, x, y, clicks=1, interval=0.0):
        if clicks <= 0:
            logging.error("Clicks must be positive integer")
            return False
        if interval < 0:
            logging.error("Interval must be non-negative")
            return False
        if not self.check_bounds(x, y):
            return False
        try:
            pyautogui.click(x=x, y=y, clicks=clicks, interval=interval)
            return True
        except pyautogui.FailSafeException:
            logging.warning("Failsafe triggered, stopping")
            return False
        except Exception as e:
            logging.error(f"Click failed: {e}")
            return False

    # Run repeated clicks handling interruptions and errors
    def handle_autoclick(self, x, y, count, delay):
        if count <= 0 or delay <= 0:
            logging.error("Count and delay must be positive")
            return
        for i in range(count):
            if not self.safe_click(x, y):
                break
            time.sleep(delay)
