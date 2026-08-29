import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name="mouse_automation", log_file="logs/app.log", level=logging.INFO, max_bytes=5242880, backup_count=3):
    """Configure logger with rotating file handler for the autoclicker."""
    logger = logging.getLogger(name)
    # Prevent adding multiple handlers if called repeatedly
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    # Create logs directory if needed
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # Add console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger