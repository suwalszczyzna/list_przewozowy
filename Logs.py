import logging


def create_logger(__name__):
    logging.basicConfig(filename='logfile.log', format='%(asctime)s : %(levelname)s : Module %(name)s : %(message)s')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
