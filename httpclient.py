import requests
import time

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
        """
        Get http request with certain method, url and block of data.

        """

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
        """
        Authorize in system. Get token and record it in 'headers' attribute.

        """
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