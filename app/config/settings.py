"""
Application Settings
"""

from app.config.environment import get_environment_variable

APP_NAME =get_environment_variable("APP_NAME");
APP_VERSION = get_environment_variable("APP_VERSION");
APP_ENV = get_environment_variable("APP_ENV");