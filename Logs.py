import logging


def create_logger(__name__):
    logging.basicConfig(
        filename='logfile.log',
        format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
