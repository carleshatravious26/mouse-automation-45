import logging
import os
from datetime import datetime

LOGGER_NAME = "mouse_automation"

def setup_logger(log_file: str = "autoclicker.log", level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns the application logger with console and file handlers.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level)

    # Avoid duplicate handlers if logger is already configured
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File output
    try:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except OSError as err:
        logger.warning(f"Could not initialize log file handler: {err}")

    return logger

def get_logger() -> logging.Logger:
    """
    Retrieves the global logger instance.
    """
    return logging.getLogger(LOGGER_NAME)

def log_click_event(x: int, y: int, button: str = "left") -> None:
    """
    Logs a simulated mouse click action with coordinates.
    """
    get_logger().info(f"Simulated click: {button.upper()} button at ({x}, {y})")

def log_status_change(running: bool) -> None:
    """
    Logs state changes of the autoclicker execution.
    """
    status = "STARTED" if running else "STOPPED"
    get_logger().info(f"Autoclicker execution status: {status}")
