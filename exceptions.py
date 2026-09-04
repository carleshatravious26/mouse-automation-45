"""Custom exception hierarchy for mouse automation application."""

from typing import Any, Optional


class AutoClickerError(Exception):
    """Base exception for all mouse automation errors."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: dict[str, Any] = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class ConfigurationError(AutoClickerError):
    """Raised when invalid configuration parameters are provided."""

    pass


class CoordinateOutOfBoundsError(AutoClickerError):
    """Raised when target click coordinates fall outside active display bounds."""

    def __init__(self, x: int, y: int, max_x: int, max_y: int) -> None:
        message: str = f"Target coordinates ({x}, {y}) exceed bounds ({max_x}x{max_y})"
        details: dict[str, int] = {"x": x, "y": y, "max_x": max_x, "max_y": max_y}
        super().__init__(message=message, details=details)


class ClickerStateError(AutoClickerError):
    """Raised when an action is performed in an invalid clicker state."""

    def __init__(self, current_state: str, attempted_action: str) -> None:
        message: str = (
            f"Cannot perform '{attempted_action}' while clicker is '{current_state}'"
        )
        details: dict[str, str] = {
            "current_state": current_state,
            "attempted_action": attempted_action,
        }
        super().__init__(message=message, details=details)


class HotkeyBindingError(AutoClickerError):
    """Raised when hotkey registration or key combination parsing fails."""

    pass
