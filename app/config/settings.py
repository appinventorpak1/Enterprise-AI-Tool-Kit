
"""
Application Settings
"""

from app.config.environment import get_environment_variable
from app.core.exceptions import ConfigurationError


# ======================
# Core Pipeline Helpers
# ======================

def read(key: str, default=None):
    """Step 1: Environment se value uthata hai"""
    return get_environment_variable(key, default)


def normalize(value):
    """Step 2: Clean karta hai (strip + empty → None)"""
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        if value == "":
            return None
    return value


def validate(value, key: str = None, required: bool = False):
    """Step 3: Basic validation"""
    if required and value is None:
        
        raise ConfigurationError(key=key, value=value, expected="Non-empty value",
                     reason="Missing required configuration")
    return value


def convert(value, converter):
    """Step 4: Convert karta hai using given strategy"""
    if value is None:
        return None
    return converter(value)


def process_setting(
    key: str,
    converter=str,
    default=None,
    required: bool = False
):
    """
    Main Pipeline:
    read → normalize → validate → convert
    """
    value = read(key, default)
    value = normalize(value)
    value = validate(value, key=key, required=required)
    value = convert(value, converter)

    if value is None:
        return default

    return value


def validate_allowed_values(key: str, value, allowed_values: list):
    """
    Extra validation for specific allowed values.
    Supports both str and int (or any type) as long as types match.
    """
    if value in allowed_values:
        return

    # Safe way to join any type of values
    allowed = "\n".join(str(v) for v in allowed_values)

    raise ConfigurationError(key=key, value=value, expected=allowed, 
            reason="Value not in allowed set")
    
    


# ======================
# Application Settings
# ======================

APP_NAME = process_setting(
    key="APP_NAME",
    converter=str,
    default="Enterprise AI Toolkit"
)

APP_VERSION = process_setting(
    key="APP_VERSION",
    converter=str,
    default="0.0.0"
)

APP_ENV = process_setting(
    key="APP_ENV",
    converter=str,
    required=True
)

UPLOAD_MAX_SIZE = process_setting(
    key="UPLOAD_MAX_SIZE",
    converter=int,
    #default=0,
    required=True
)

# Extra validation for APP_ENV
validate_allowed_values(
    key="APP_ENV",
    value=APP_ENV,
    allowed_values=["Development", "Testing", "Staging", "Production"]
)

validate_allowed_values(
    key="UPLOAD_MAX_SIZE",
    value=UPLOAD_MAX_SIZE,
    allowed_values=[10, 20, 50, 100]
)