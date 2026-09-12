class MouseAutomationError(Exception):
    """Base exception for the mouse-automation-45 package."""
    pass

class ClickExecutionError(MouseAutomationError):
    """Raised when an autoclick operation fails to execute."""
    def __init__(self, message: str, coordinate: tuple[int, int]) -> None:
        super().__init__(f"{message} at {coordinate}")
        self.coordinate = coordinate

class ConfigurationError(MouseAutomationError):
    """Raised when provided settings are invalid or out of bounds."""
    def __init__(self, setting: str, value: float) -> None:
        super().__init__(f"Invalid value '{value}' for setting '{setting}'")
        self.setting = setting

class HardwareAccessError(MouseAutomationError):
    """Raised when the system blocks input simulation."""
    def __init__(self, message: str = "Permission denied for input simulation") -> None:
        super().__init__(message)

class IntervalTimingError(MouseAutomationError):
    """Raised when the requested click frequency is impossible."""
    def __init__(self, interval: float) -> None:
        super().__init__(f"Frequency constraint violation: {interval}s is too fast")
        self.interval = interval