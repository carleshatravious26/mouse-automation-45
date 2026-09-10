import json
import os
from typing import Dict, Any

def save_click_profile(filename: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to a local JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Storage error: {e}")
        return False

def load_click_profile(filename: str) -> Dict[str, Any]:
    """Retrieves autoclicker settings from a JSON file."""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Retrieval error: {e}")
        return {}

def validate_settings(settings: Dict[str, Any]) -> bool:
    """Checks configuration integrity for autoclick operations."""
    required = {'interval', 'button', 'clicks'}
    return all(key in settings for key in required)