import time
from typing import Any, Dict, List, Optional


class AutoClickerCore:
    """Core execution loop for mouse automation with task input validation."""

    ALLOWED_BUTTONS = {"left", "right", "middle"}

    def __init__(self, default_interval: float = 0.1) -> None:
        self.default_interval = default_interval
        self.is_running = False

    def validate_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Validates and sanitizes a single click task payload."""
        if not isinstance(task, dict):
            raise ValueError("Task payload must be a dictionary")

        interval = task.get("interval", self.default_interval)
        if not isinstance(interval, (int, float)) or interval <= 0:
            raise ValueError(f"Invalid interval: {interval}. Must be a positive number.")

        button = task.get("button", "left")
        if not isinstance(button, str) or button.lower() not in self.ALLOWED_BUTTONS:
            raise ValueError(f"Invalid mouse button: {button}. Must be one of {self.ALLOWED_BUTTONS}")

        clicks = task.get("clicks", 1)
        if not isinstance(clicks, int) or clicks <= 0:
            raise ValueError(f"Invalid click count: {clicks}. Must be a positive integer.")

        pos = task.get("position")
        if pos is not None:
            if not (isinstance(pos, (tuple, list)) and len(pos) == 2):
                raise ValueError("Position must be a tuple or list of two integers (x, y)")
            x, y = pos
            if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
                raise ValueError("Coordinates x and y must be non-negative integers")

        return {
            "interval": float(interval),
            "button": button.lower(),
            "clicks": clicks,
            "position": tuple(pos) if pos else None
        }

    def process_queue(self, task_queue: List[Dict[str, Any]]) -> int:
        """Main processing loop that validates and executes queued click tasks."""
        self.is_running = True
        executed_count = 0

        for raw_task in task_queue:
            if not self.is_running:
                break

            try:
                valid_task = self.validate_task(raw_task)
            except ValueError as err:
                print(f"[Core Warning] Skipping invalid task: {err}")
                continue

            pos_str = f"at {valid_task['position']}" if valid_task["position"] else "at current cursor"
            print(f"Executing: {valid_task['clicks']} {valid_task['button']} click(s) {pos_str}")
            time.sleep(valid_task["interval"])
            executed_count += 1

        self.is_running = False
        return executed_count