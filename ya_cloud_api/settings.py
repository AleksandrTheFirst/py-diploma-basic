import configparser

class YaCloudConfig:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.app_id = config['VKAPI']['app_id']
        self.user_id = config['VKAPI']["user_id"]
        self.token = config['VKAPI']["access_token"]


cfg = YaCloudConfig()
print(cfg.app_id)