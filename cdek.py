import requests


class Cdek:
    

    token = ''
    headers = ''
    test = False

    def __init__(self, account, secret_key):
        self.account = account
        self.secret_key = secret_key

    def get_token(self):

        response = requests.post(url=self.get_url() + 'oauth/token',
                                 data={'grant_type': 'client_credentials', 'client_id': self.account,
                                       'client_secret': self.secret_key})
        data = response.json()

        self.token = data['access_token']
        self.headers = {'Authorization' : 'Bearer ' + self.token}

    def get_url(self):
        if self.test:
            return 'https://api.edu.cdek.ru/v2/'
        else:
            return 'https://api.cdek.ru/v2/'

    def get_order(self, uuid_number):
        response = requests.get(url = self.get_url() + 'orders/' + uuid_number, headers = self.headers)
        return response.json()

    def new_order(self, data):
        response = requests.post(url = self.get_url() + 'orders', data = data)
        return response.json()


