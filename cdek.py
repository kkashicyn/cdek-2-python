from httpclient import HttpClient

class Cdek:
    http = object

    def __init__(self, account, secret_key):
        self.http = HttpClient(account=account, secret_key=secret_key)

    def get_order(self, uuid_number):
        return self.http.request(url='orders/' + uuid_number, method='get')

    def new_order(self, data):
        return self.http.request(url='orders', data=data, method='post')

    def edit_order(self, data):
        return self.http.request(url='orders', data=data, method='patch')

    def delete_order(self, uuid_number):
        return self.http.request(url='orders/' + uuid_number, method='delete')

