import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

@dataclass
class ClickConfig:
    interval: float = 0.5
    random_variance: float = 0.1
    button: str = "left"
    click_count: int = 1
    hold_duration: float = 0.0

@dataclass
class AppConfig:
    click_config: ClickConfig
    hotkey_start: str = "f6"
    hotkey_stop: str = "f7"
    config_path: str = "autoclicker_config.json"
    log_level: str = "INFO"

    def to_dict(self):
        return {
            "click_config": asdict(self.click_config),
            "hotkey_start": self.hotkey_start,
            "hotkey_stop": self.hotkey_stop,
            "config_path": self.config_path,
            "log_level": self.log_level,
        }

class ConfigManager:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path or "autoclicker_config.json")
        self.config = self._create_default_config()

    def _create_default_config(self):
        return AppConfig(click_config=ClickConfig(), hotkey_start="f6", hotkey_stop="f7", config_path=str(self.config_path), log_level="INFO")

    def load_config(self):
        if not self.config_path.exists():
            self.config = self._create_default_config()
            return self.config
        try:
            with open(self.config_path, "r") as f:
                data = json.load(f)
            click_data = data.get("click_config", {})
            click_config = ClickConfig(interval=click_data.get("interval", 0.5), random_variance=click_data.get("random_variance", 0.1), button=click_data.get("button", "left"), click_count=click_data.get("click_count", 1), hold_duration=click_data.get("hold_duration", 0.0))
            self.config = AppConfig(click_config=click_config, hotkey_start=data.get("hotkey_start", "f6"), hotkey_stop=data.get("hotkey_stop", "f7"), config_path=data.get("config_path", str(self.config_path)), log_level=data.get("log_level", "INFO"))
        except (json.JSONDecodeError, IOError, KeyError) as e:
            print(f"Config load error: {e}. Using defaults.")
            self.config = self._create_default_config()
        return self.config

    def save_config(self):
        data = self.config.to_dict()
        with open(self.config_path, "w") as f:
            json.dump(data, f, indent=2)

    def update_click_config(self, **updates):
        for key, value in updates.items():
            if hasattr(self.config.click_config, key):
                setattr(self.config.click_config, key, value)

    def get_config(self):
        return self.config