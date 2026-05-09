import logging
import os

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs', 'trading_bot.log'))

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    fh = logging.FileHandler(log_path)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger