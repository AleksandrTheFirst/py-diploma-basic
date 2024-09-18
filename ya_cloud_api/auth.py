class Auth:
    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}

