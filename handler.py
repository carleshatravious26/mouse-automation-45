import time
from typing import Optional, Tuple
import pyautogui

class ClickHandler:
    """Handles mouse click automation for the autoclicker."""

    def __init__(self, interval: float = 0.5, clicks: int = 1, button: str = "left") -> None:
        """Set up the handler with click parameters.

        Args:
            interval: Seconds to wait between click sequences.
            clicks: How many times to click each sequence.
            button: Which mouse button to use for clicks.
        """
        self.interval: float = interval
        self.clicks: int = clicks
        self.button: str = "left"
        self._is_running: bool = False

    def start(self, duration: Optional[float] = None) -> None:
        """Launch the continuous clicking loop.

        Args:
            duration: Maximum seconds to continue. Infinite if not provided.
        """
        self._is_running = True
        start_time = time.time()
        while self._is_running:
            if duration is not None and time.time() - start_time >= duration:
                self.stop()
                break
            # Perform automated mouse click
            pyautogui.click(clicks=self.clicks, button=self.button)
            time.sleep(self.interval)

    def stop(self) -> None:
        """Terminate the clicking activity immediately."""
        self._is_running = False

    def move_to(self, x: int, y: int) -> None:
        """Relocate the mouse pointer to given screen coordinates.

        Args:
            x: X-axis position on screen.
            y: Y-axis position on screen.
        """
        pyautogui.moveTo(x, y)

    def get_position(self) -> Tuple[int, int]:
        """Fetch the present mouse pointer coordinates.

        Returns:
            Tuple containing x and y integer values.
        """
        position = pyautogui.position()
        return position.x, position.y


def initialize_handler(interval: float, clicks: int, button: str) -> ClickHandler:
    """Instantiate a configured click handler.

    Args:
        interval: Delay between actions.
        clicks: Repetitions per action.
        button: Button identifier.

    Returns:
        Ready-to-use ClickHandler object.
    """
    return ClickHandler(interval=interval, clicks=clicks, button=button)
