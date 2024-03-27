import os
from configparser import ConfigParser
from utility.misc import get_project_folder_path


def read_config(section, key):
    config = ConfigParser()
    config_file_path = os.path.join(get_project_folder_path(), 'conf.ini')
    config.read(config_file_path)
    # config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section, key)


def locator_reader(file_name, locator_id):
    pass
