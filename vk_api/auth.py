from settings import VKConfig

class Auth:
    def __init__(self):
        cfg = VKConfig()
        self.access_token = cfg.token
        self.user_id = cfg.user_id
        self.app_id = cfg.app_id

    def get_attr(self, name):
        return self.__dict__[name] if name in self.__dict__ else f'No attribute with name {name}'
