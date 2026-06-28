import yaml


def load_config():

    with open(
        "config/config.yaml",
        "r",
        encoding="utf-8",
    ) as file:

        return yaml.safe_load(file)
