import os
from typing import Dict, Any
import json

# Default autoclicker configuration settings
DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat_times": 100,
    "hotkey": "f6",
    "randomization": False
}

CONFIG_FILE_PATH = "settings.json"

def load_app_config() -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults if missing."""
    if not os.path.exists(CONFIG_FILE_PATH):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_app_config(config: Dict[str, Any]) -> None:
    """Persists current configuration to the local filesystem."""
    try:
        with open(CONFIG_FILE_PATH, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

# UI and logic constants
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0
SUPPORTED_BUTTONS = ["left", "right", "middle"]
APP_VERSION = "1.2.0"