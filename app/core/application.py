from app.config.settings import APP_NAME, APP_VERSION
from app.core.logger import logger
import logging

logger = logging.getLogger(__name__)


class Application:
    def start(self):
        print("=" * 60)
        print(APP_NAME)
        print(f"Version : {APP_VERSION}")
        print("=" * 60)
        
        logger.info("Application Started Successfully")
        