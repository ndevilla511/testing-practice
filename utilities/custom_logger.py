import inspect
import logging


def get_logger(log_level=logging.DEBUG):

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    logger.setLevel(log_level)

    fileHandler = logging.FileHandler('logfile.log', mode="a")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # file handler object

    return logger
