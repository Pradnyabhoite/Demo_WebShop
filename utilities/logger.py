import logging
import os
from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(
            log_dir,
            f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger