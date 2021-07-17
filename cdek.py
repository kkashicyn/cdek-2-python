import json
import requests


class Cdek:
    
    url = 'https://api.cdek.ru/v2/'
    token = ''
    
    def __init__(self, account, secret_key):
        self.account = account
        self.secret_key = secret_key
        response = requests.get(url = self.url + 'oauth/token')
        data = json.loads(response.text)
        self.token = data['access_token']
        
        
