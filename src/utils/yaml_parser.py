import pyyaml
import os

class YAMLParser:
    """
    Responsible for parsing YAML configuration files.
    """
    @staticmethod
    def parse(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file not found at {file_path}")
        try:
            with open(file_path, 'r') as config_file:
                return pyyaml.safe_load(config_file)
        except pyyaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file {file_path}: {e}")
