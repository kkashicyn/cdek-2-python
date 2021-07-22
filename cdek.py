import requests
import time


class Cdek:
    http = object

    def __init__(self, account, secret_key):
        self.http = HttpClient(account=account, secret_key=secret_key)

    def new_order(self, data):
        return self.http.request(url='orders', method='post', data=data)

    def get_order(self, uuid_number):
        return self.http.request(url='orders/' + uuid_number, method='get')

    def delete_order(self, uuid_number):
        return self.http.request(url='orders/', method='delete', data={'uuid_number': uuid_number})


class HttpClient:
    account = ''
    secret_key = ''
    headers = {}
    time_expired = 0
    url = 'https://api.cdek.ru/v2/'

    def __init__(self, account, secret_key):

        self.account = account
        self.secret_key = secret_key

    def request(self, url, method, data=None):
        try:
            if self.is_expired():
                self.auth()
            if method == 'post' or method == 'patch':
                self.headers['Content-Type'] = 'application/json'
            response = requests.request(method=method, url=self.url + url, json=data, headers=self.headers)
            return response.json()
        except Exception as e:
            print(e)

    def auth(self):
        try:
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
            data = requests.post(url=self.url + 'oauth/token', headers=self.headers,
                                 data={'grant_type': 'client_credentials',
                                       'client_id': self.account,
                                       'client_secret': self.secret_key},
                                 )
            self.headers['Authorization'] = 'Bearer ' + data.json()['access_token']
        except Exception as e:
            print(e)

    def is_expired(self):
        if self.time_expired - time.time() > 0:
            return False
        else:
            return True

    def set_test(self, is_test):
        if is_test:
            self.url = 'https://api.edu.cdek.ru/v2/'
        else:
            self.url = 'https://api.cdek.ru/v2/'