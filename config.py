import yaml


class Config():
    """
    init config with other directory file like Config("config/setting.yaml")

    .__dict__ to get all value config as dictionary
    """
    def __init__(self, path="config.yaml", key=None, value=None):
        with open(path, "r", encoding="utf8") as f:
            data = yaml.safe_load(f)
        for key, value in data.items():
            setattr(self, key, value)


config = Config()

if __name__ == "__main__":
    config = Config("config/setting.yaml")
    print(config.__dict__)
