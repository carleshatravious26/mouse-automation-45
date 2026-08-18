import time
import threading
from typing import Optional

class AutoClicker:
    def __init__(self, interval: float):
        """Initialize the AutoClicker.
        
        Args:
            interval (float): Time in seconds between clicks.
        """
        self.interval = interval
        self.running = False
        self.click_thread: Optional[threading.Thread] = None

    def start(self) -> None:
        """Start the auto clicker in a separate thread."""
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def stop(self) -> None:
        """Stop the auto clicker."""
        self.running = False
        if self.click_thread:
            self.click_thread.join()
            self.click_thread = None

    def _click_loop(self) -> None:
        """Run the clicking loop until stopped."""
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self) -> None:
        """Perform the click action (stub)."""
        print("Mouse clicked!")

if __name__ == '__main__':
    clicker = AutoClicker(interval=1.0)
    clicker.start()
    time.sleep(5)  # Let it click for 5 seconds
    clicker.stop()