import os


def get_project_folder_path():
    # Get the path of the current script
    current_file_path = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(current_file_path))
