import json
import requests


class Cdek:
    
    url = 'https://api.cdek.ru/v2/'
    token = ''
    headers = ''
    
    def __init__(self, account, secret_key):
        self.account = account
        self.secret_key = secret_key
        response = requests.post(url = self.url + 'oauth/token', data = {'grant_type': 'client_credentials', 'client_id' : self.account, 'client_secret': self.secret_key})
        data = json.loads(response.text)
        self.token = data['access_token']
        self.headers = {'Authorization' : 'Bearer ' + self.token}

    def get_order(self, uuid_number):

        response = requests.get(url = self.url + 'orders/' + uuid_number, headers = self.headers)
        data = json.loads(response.text)
        return data

    def new_order(self, params):
        requests.post(url = '', data = params)
        pass
