import logging
import os
import time


class Logger:

    def __init__(self, logger_name, file_level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        # Get the path of the current script
        current_file_path = os.path.abspath(__file__)

        # Navigate up to the project directory
        project_dir = os.path.dirname(os.path.dirname(current_file_path))

        log_dir = os.path.join(project_dir, 'Logs')  # Path to the log directory
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Construct the path to the log file
        curr_time = time.strftime("%Y-%m-%d")
        log_file_name = 'log' + curr_time + '.txt'
        log_file_path = os.path.join(log_dir, log_file_name)

        # "a" to append the logs in the same file, "w" to generate new logs and delete the old ones
        fh = logging.FileHandler(log_file_path, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
