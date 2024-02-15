import yaml

CONFIG_PATH = "./config/config.yaml"


def get_config():
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)


def print_config():
    with open(CONFIG_PATH, 'r') as file:
        conf = yaml.safe_load(file)

    for line in conf:
        print(line)
