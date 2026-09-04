class AutoclickerError(Exception):
    """Base exception for mouse-automation-45."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when settings fail validation."""
    pass

class ClickerRuntimeError(AutoclickerError):
    """Raised during active clicker operation."""
    pass

class InputValidationError(AutoclickerError):
    """Raised when user input for intervals is invalid."""
    pass

def validate_interval(interval: float):
    """Ensures click interval is within safe bounds."""
    if interval < 0.01:
        raise InputValidationError("Interval must be at least 0.01 seconds.")
    if interval > 60.0:
        raise InputValidationError("Interval cannot exceed 60 seconds.")

def validate_coordinates(x: int, y: int):
    """Checks if coordinates are non-negative."""
    if x < 0 or y < 0:
        raise InputValidationError("Coordinates must be positive integers.")