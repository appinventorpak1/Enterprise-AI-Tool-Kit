"""
Application Settings
"""

from app.config.environment import get_environment_variable


def validate_allowed_values(
    key: str,
    value: str,
    allowed_values: list[str]
):
    if value in allowed_values:
        return

    allowed = "\n".join(allowed_values)
    raise ValueError(
        f"Invalid value for '{key}'.\n\n"
        f"Current Value:\n{value}\n\n"
        f"Allowed Values:\n{allowed}"
    )


def get_required_setting(key: str) -> str:
    value = get_environment_variable(key)

    if value is None or not value.strip():
        raise ValueError(
            f"Required configuration '{key}' is missing."
        )

    return value

APP_NAME = get_environment_variable(
    "APP_NAME",
    "Enterprise AI Toolkit"
)
APP_VERSION = get_environment_variable("APP_VERSION");
APP_ENV = get_required_setting("APP_ENV");

validate_allowed_values(
    key="APP_ENV",
    value=APP_ENV,
    allowed_values=["Development", "Testing", "Staging", "Production"]
)