import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name="autoclicker", log_file="logs/autoclicker.log", max_bytes=1048576, backup_count=5, level=logging.INFO):
    """Configures and returns a logger with both console and rotating file output."""
    # Create log directory if it does not exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is imported multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console logging handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

        # Rotating file logging handler
        try:
            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(level)
            logger.addHandler(file_handler)
        except IOError as err:
            logger.warning(f"Could not initialize file logging: {err}")

    return logger

# Initialize default logger instance for immediate use across the application
logger = setup_logger()
