class MouseAutomationError(Exception):
    """Base exception for all mouse-automation-45 errors."""
    pass

class HardwareInteractionError(MouseAutomationError):
    """Raised when low-level mouse control fails."""
    pass

class ConfigurationError(MouseAutomationError):
    """Raised when provided config parameters are invalid."""
    pass

class ExecutionTimeoutError(MouseAutomationError):
    """Raised when an automation sequence hangs."""
    pass

class InterruptSignal(MouseAutomationError):
    """Raised when the user triggers a manual stop."""
    pass

def handle_automation_exception(e: Exception) -> None:
    """Helper to format and log automation specific errors."""
    if isinstance(e, MouseAutomationError):
        print(f"[Automation Error]: {type(e).__name__} - {e}")
    else:
        print(f"[Unexpected Error]: {e}")