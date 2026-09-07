import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,  # seconds
    "button": "left",  # left, right, middle
    "click_type": "single",  # single, double
    "hotkey_start": "F7",
    "hotkey_stop": "F8",
    "repeat_count": 0,  # 0 for infinite
}


class ConfigManager:
    """Manages loading, saving, and updating configurations for the autoclicker."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.settings = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or falls back to defaults."""
        if not os.path.exists(self.filepath):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                # Ensure all default keys exist in the loaded config
                for key, val in DEFAULT_CONFIG.items():
                    data.setdefault(key, val)
                return data
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Saves the configuration dictionary to a file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(config_data, f, indent=4)
            self.settings = config_data
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def get(self, key: str) -> Any:
        """Retrieves a configuration value safely."""
        return self.settings.get(key, DEFAULT_CONFIG.get(key))

    def update(self, key: str, value: Any) -> None:
        """Updates a config setting and writes to storage."""
        self.settings[key] = value
        self.save_config(self.settings)
