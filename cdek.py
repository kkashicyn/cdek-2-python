import requests


class Cdek:
    
    httpclient = object

    def __init__(self, account, secret_key):
        self.httpclient = HttpClient(account=account, secret_key=secret_key)

    def get_order(self, uuid_number):
        return self.httpclient.request(url='orders/', method='get', data={'uuid_number': uuid_number})

    def new_order(self, data):
        return self.httpclient.request(url='orders', method='post', data=data)


class HttpClient:
    test = False
    account = ''
    secret_key = ''
    headers = {}
    token = ''

    def __init__(self, account, secret_key):
        self.account = account
        self.secret_key = secret_key

    def request(self, url, method, params=None, data=None):
        try:
            if method == 'get':
                response = requests.get(url=self.get_url() + url, params=data, headers=self.headers)
            elif method == 'post':
                if url == 'oauth/token':
                    self.headers['Content-Type'] = 'application/x-www-form-urlencoded'

                    response = requests.post(url=self.get_url() + url, data=data, headers=self.headers)
                    self.token = response.json()['access_token']
                    self.headers['Authorization'] = 'Bearer ' + self.token
                else:
                    self.headers['Content-Type'] = 'application/json'
                    response = requests.post(url=self.get_url() + url, json=data, headers=self.headers)

            return response.json()
        except Exception as e:
            print(e)

    def get_token(self):
        self.request(url='oauth/token', method='post', data={'grant_type': 'client_credentials',
                                                                 'client_id': self.account,
                                                                 'client_secret': self.secret_key})

    def get_url(self):
        if self.test:
            return 'https://api.edu.cdek.ru/v2/'
        else:
            return 'https://api.cdek.ru/v2/'
