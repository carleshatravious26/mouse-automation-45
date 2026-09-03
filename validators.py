import re
from typing import Any, Dict, Optional

def validate_click_config(config: Dict[str, Any]) -> bool:
    """
    Validates that the provided configuration has the required fields
    and correct data types for the autoclicker engine.
    """
    required_fields = {
        "interval": (float, int),
        "button": str,
        "coordinates": tuple
    }

    for field, expected_type in required_fields.items():
        if field not in config:
            return False
        if not isinstance(config[field], expected_type):
            return False

    # Validate coordinates are positive integers
    x, y = config["coordinates"]
    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        return False

    # Validate interval is a positive value
    if config["interval"] <= 0:
        return False

    return True

def sanitize_hotkey(key: str) -> Optional[str]:
    """
    Sanitizes hotkey input to ensure it matches standard
    keyboard event formats.
    """
    pattern = r'^[a-z0-9_]{1,10}$'
    if re.match(pattern, key.lower()):
        return key.lower()
    return None