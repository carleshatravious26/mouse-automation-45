import time
import pyautogui

# Eliminate built-in pauses for better performance
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

class OptimizedAutoclicker:
    def __init__(self, clicks_per_second=10):
        self.interval = 1.0 / clicks_per_second
        self.last_time = 0

    def click(self, x, y):
        current_time = time.perf_counter()
        if self.last_time > 0 and current_time - self.last_time < self.interval:
            time.sleep(self.interval - (current_time - self.last_time))
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click(x=x, y=y)
        self.last_time = time.perf_counter()

    def batch_click(self, positions):
        for x, y in positions:
            self.click(x, y)

    def run_for_duration(self, x, y, duration_seconds):
        end_time = time.perf_counter() + duration_seconds
        while time.perf_counter() < end_time:
            self.click(x, y)

def create_clicker(cps):
    return OptimizedAutoclicker(cps)

def precompute_click_positions(base_x, base_y, num, offset=5):
    pos_list = [(base_x + i * offset, base_y) for i in range(num)]
    return pos_list