from pprint import pprint

import requests
from auth import Auth


class VK:
    def __init__(self, access_token, user_id, version='5.199'):
        self.version = version
        self.user_id = user_id
        self.access_token = access_token
        self.base_address = 'https://api.vk.com/method/'
        self.params = {'access_token': self.access_token, 'v': self.version}

    def user_info(self):
        url = f'{self.base_address}users.get'
        params = {'user_ids': self.user_id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def photos_info(self):
        url = f'{self.base_address}photos.get'
        params = {'owner_id': self.user_id, 'extended': 1, 'album_id': 'profile'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

auth = Auth()
vk = VK(auth.get_attr('access_token'), auth.get_attr('user_id'))
pprint(vk.photos_info())