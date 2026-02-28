import yaml
import os

def load_config():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, "config.yaml")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise Exception("config.yaml is empty or invalid")

    return config