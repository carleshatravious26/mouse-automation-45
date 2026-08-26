import logging
from typing import Optional

class AutoClickerLogger:
    """Handles logging for mouse automation events and errors."""
    
    def __init__(self, name: str = "mouse_automation", level: int = logging.INFO) -> None:
        """Initialize the logger with a specific name and log level."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log an informational message about clicker actions."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = None) -> None:
        """Log an error message during automation execution."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log a warning message for unexpected states."""
        self.logger.warning(message)
