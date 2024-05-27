from loguru import logger
from datetime import datetime as dt


class Logger:
    def __call__(self):
        name = (str(dt.now()) + '.log').replace(':', '-')
        logger.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=rf"./Logs/{name}"
        )

    def info(self, message):
        logger.info(message)

    def error(self, message):
        logger.error(message)

    def warning(self, message):
        logger.warning(message)

    def critical(self, message):
        logger.critical(message)
