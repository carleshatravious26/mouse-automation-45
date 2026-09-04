class AutomationError(Exception):
    """Base exception for all mouse-automation-45 errors."""
    pass

class ConfigError(AutomationError):
    """Raised when configuration validation fails."""
    pass

class DeviceNotFoundError(AutomationError):
    """Raised when target input device is unavailable."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when a click sequence exceeds allowed duration."""
    pass

class PermissionDeniedError(AutomationError):
    """Raised when operating system denies input control."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when click frequency exceeds safety thresholds."""
    pass

def raise_if_none(value, message):
    """Utility to enforce non-null values in core logic."""
    if value is None:
        raise AutomationError(message)

def validate_permission(granted):
    """Ensures system access rights before automation start."""
    if not granted:
        raise PermissionDeniedError("Access to system input controls blocked")