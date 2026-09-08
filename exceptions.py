class AutoclickerError(Exception):
    """Base exception for all mouse-automation-45 errors."""

class ConfigurationError(AutoclickerError):
    """Raised when the settings file is invalid or missing."""

class MouseControlError(AutoclickerError):
    """Raised when low-level mouse input simulation fails."""

class HotkeyRegistrationError(AutoclickerError):
    """Raised when the system fails to bind the trigger key."""

class DataValidationError(AutoclickerError):
    """Raised when user input for click intervals is invalid."""

class ProcessInterruptError(AutoclickerError):
    """Raised when the automation process is forced to stop."""

if __name__ == '__main__':
    # Internal validation of exception structure
    try:
        raise ConfigurationError("Settings file not found")
    except AutoclickerError as e:
        print(f"Caught expected exception: {e}")