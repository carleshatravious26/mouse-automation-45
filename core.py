import time

class CoreAutoClicker:
    """Core autoclicker module with performance optimizations."""

    def __init__(self, clicks_per_second=10):
        self.clicks_per_second = clicks_per_second
        self.interval = 1.0 / clicks_per_second
        self.running = False
        self.clicks_done = 0

    def start(self, max_clicks=None, max_duration=None):
        """Start optimized autoclick loop.
        Uses high-resolution timer to maintain precise click rate
        without cumulative timing errors.
        """
        self.running = True
        self.clicks_done = 0
        start = time.perf_counter()
        target = start

        while self.running:
            now = time.perf_counter()

            if max_clicks is not None and self.clicks_done >= max_clicks:
                break
            if max_duration is not None and (now - start) >= max_duration:
                break

            self.click()
            self.clicks_done += 1

            target += self.interval
            sleep_time = target - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)

    def click(self):
        # Actual implementation would use mouse automation library
        # e.g. from pynput.mouse import Button, Controller
        # mouse = Controller()
        # mouse.click(Button.left, 1)
        print("Mouse click executed")

    def stop(self):
        self.running = False