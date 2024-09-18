import requests
from auth import Auth

class Folder(Auth):
    def __init__(self, token):
        super().__init__(token)

    def create_folder(self, folder_name):
        response = requests.put('123123', headers=self.headers, params={'path': folder_name})
        return response.status_code
