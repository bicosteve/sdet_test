import logging


class LogGenerator:
    @staticmethod
    def denerate_logs():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(f"%(asctime)s - %(levelname)s - %(message)s")
        file_handler = logging.FileHandler("./logs/log.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
