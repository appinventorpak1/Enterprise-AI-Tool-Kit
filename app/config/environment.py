import os

from dotenv import load_dotenv

load_dotenv()


def get_environment_variable(key: str, default: str | None = None):
    return os.getenv(key, default)