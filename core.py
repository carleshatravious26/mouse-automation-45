"""Core functionality for the mouse autoclicker."""
import time
from typing import Optional
import pyautogui

# Use pyautogui for cross-platform mouse control

class Autoclicker:
    """Automatic mouse clicker for automation tasks."""

    def __init__(self, clicks_per_second: float = 1.0, button: str = "left") -> None:
        """Initialize autoclicker with specified rate and button.

        Args:
            clicks_per_second: Frequency of clicks.
            button: Which mouse button to use.
        """
        if clicks_per_second <= 0:
            raise ValueError("Clicks per second must be positive")
        self.interval: float = 1.0 / clicks_per_second
        self.button: str = button
        self.running: bool = False

    def start(self, duration: Optional[float] = None) -> None:
        """Begin the clicking loop.

        Args:
            duration: How long to click in seconds. None means run until stopped.
        """
        self.running = True
        start_time: float = time.time()
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)
            if duration is not None:
                if time.time() - start_time >= duration:
                    self.stop()

    def stop(self) -> None:
        """Halt the autoclicker."""
        self.running = False


def run_autoclicker(clicks_per_second: float = 5.0, duration: float = 5.0) -> None:
    """Run the autoclicker with given parameters.

    Args:
        clicks_per_second: Clicks frequency.
        duration: Total run time in seconds.
    """
    clicker = Autoclicker(clicks_per_second=clicks_per_second)
    try:
        clicker.start(duration=duration)
    except KeyboardInterrupt:
        # Handle user interruption gracefully
        clicker.stop()
        print("Autoclicker stopped by user.")


if __name__ == "__main__":
    run_autoclicker()