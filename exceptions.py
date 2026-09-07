class MouseAutomationError(Exception):
    """Base exception for all mouse-automation-45 issues."""

class ConfigurationError(MouseAutomationError):
    """Raised when user-defined settings are invalid."""

class ClickerRuntimeError(MouseAutomationError):
    """Raised during active click execution failures."""

class PermissionDeniedError(MouseAutomationError):
    """Raised when the OS denies accessibility permissions."""

def validate_settings(settings: dict):
    """Ensures configuration values are within logical bounds."""
    if settings.get("interval", 0) < 0.001:
        raise ConfigurationError("Interval too low; must be at least 1ms.")
    
    if not isinstance(settings.get("coords"), (tuple, list)) or len(settings["coords"]) != 2:
        raise ConfigurationError("Coordinates must be a (x, y) tuple.")

def handle_execution_failure(e: Exception):
    """Centralized error reporting for runtime failures."""
    if isinstance(e, PermissionDeniedError):
        print("Error: Check OS accessibility permissions.")
    elif isinstance(e, ConfigurationError):
        print(f"Config Error: {e}")
    else:
        print(f"Unexpected error occurred: {e}")
