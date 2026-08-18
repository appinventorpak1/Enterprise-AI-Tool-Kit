from typing import Any

from .base import ApplicationError


class ConfigurationError(ApplicationError):
    """Raised when application configuration is missing or invalid."""

    def __init__(
        self,
        message: str = "",
        *,
        key: str | None = None,
        value: Any = None,
        expected: str | None = None,
        reason: str | None = None,
    ) -> None:
        self.key = key
        self.value = value
        self.expected = expected
        self.reason = reason

        if not message:
            message = self._build_message()

        super().__init__(message)

    def _build_message(self) -> str:
        parts: list[str] = []

        if self.key:
            parts.append(f"Invalid configuration for '{self.key}'")
        else:
            parts.append("Configuration error")

        if self.reason:
            parts.append(self.reason)

        if self.expected is not None:
            parts.append(f"(expected: {self.expected})")

        # Note: `value` is intentionally not included in the auto-generated
        # message to avoid accidental leakage of secrets.

        return " — ".join(parts)
