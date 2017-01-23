import logging


log = logging.getLogger(__name__)


def setup_root_logger_handler():
    """
    This method sets formatter for root logger
    @return:
    """
    root_logger = logging.getLogger()
    formatter = logging.Formatter(fmt='[%(levelname)s] - %(asctime)s - %(funcName)s() - %(message)s',
                                  datefmt='%b %d, %Y %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    root_logger.setLevel(logging.INFO)
    root_logger.handlers = [handler]