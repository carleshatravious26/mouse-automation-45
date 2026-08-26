import json
import os
from typing import Dict, Any, Optional

DEFAULTS: Dict[str, Any] = {
    "interval": 0.1,
    "button": "left",
    "clicks": 1,
    "duration": None,
    "hotkey": "ctrl+alt+s",
    "positions": []
}

class ConfigLoader:
    """Handles loading and saving configuration for mouse automation."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        """Load configuration, applying defaults where missing."""

        config = DEFAULTS.copy()

        if os.path.isfile(self.filepath):

            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    loaded = json.load(f)

                if isinstance(loaded, dict):
                    config.update(loaded)

            except (json.JSONDecodeError, OSError) as exc:
                print(f"Config load error: {exc}. Defaults applied.")

        else:
            self._save(config)

        return config

    def _save(self, data: Dict[str, Any]) -> None:
        """Write configuration to disk."""

        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, sort_keys=True)

        except OSError as exc:
            print(f"Config save error: {exc}")

    def get(self, key: str, fallback: Optional[Any] = None) -> Any:
        """Retrieve a config value or fallback."""

        return self.config.get(key, fallback)

    def set(self, key: str, value: Any) -> None:
        """Update a value and persist the config."""

        self.config[key] = value
        self._save(self.config)

    def get_all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""

        return self.config.copy()

# Usage example for the autoclicker

if __name__ == "__main__":
    loader = ConfigLoader()
    print("Loaded interval:", loader.get("interval"))
    loader.set("interval", 0.2)
    print("Updated config:", loader.get_all())