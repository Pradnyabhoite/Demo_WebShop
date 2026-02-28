import logging
import os
from datetime import datetime


class LogGenerator:

    @staticmethod
    def loggen():

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(
            log_dir,
            f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger