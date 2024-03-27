import os
import logging
from datetime import datetime

from utility.misc import get_project_folder_path


def setup_logger():
    project_dir = get_project_folder_path()
    logs_dir = os.path.join(project_dir, 'logs')  # Path to the log directory
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create log file name based on current date
    log_file = os.path.join(logs_dir, f"app_{datetime.now().strftime('%Y-%m-%d')}.log")

    # Configure logger
    logger = logging.getLogger('my_app')
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        # Log to file
        file_handler = logging.FileHandler(log_file, mode="a")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Log to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# t_logger = setup_logger()
# t_logger.info('test log')
# t_logger.debug('test debug log')