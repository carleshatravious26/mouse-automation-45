import time
from dataclasses import dataclass
from typing import List, Tuple, Optional, Callable

@dataclass
class MouseAction:
    """Represents a simulated mouse action command with delay details."""
    action_type: str  # E.g., 'click', 'double_click', 'move'
    coords: Tuple[int, int]  # Screen coordinates as (x, y)
    delay: float  # Idle time in seconds to wait after execution
    button: str = "left"  # Target mouse button: 'left', 'right', or 'middle'

class ActionProcessor:
    """Processes scheduled mouse actions and manages timing loops sequentially."""

    def __init__(self, callback: Optional[Callable[[str, Tuple[int, int]], None]] = None) -> None:
        """Initializes the processor with an optional callback for click simulation."""
        self.callback = callback
        self._active: bool = False

    def execute(self, action: MouseAction) -> bool:
        """Simulates execution of a single action and runs the post-delay."""
        if not self._active:
            return False
        
        # Trigger callback if defined (typically pointing to pyautogui/pynput wrapper)
        if self.callback:
            self.callback(action.action_type, action.coords)
            
        time.sleep(action.delay)
        return True

    def run_queue(self, queue: List[MouseAction]) -> int:
        """Sequentially executes a queue of mouse actions.

        Returns the count of successfully executed tasks.
        """
        self._active = True
        executed = 0
        try:
            for action in queue:
                if not self._active:
                    break
                if self.execute(action):
                    executed += 1
        finally:
            self._active = False
        return executed

    def stop(self) -> None:
        """Interrupts and stops the current queue execution loop."""
        self._active = False