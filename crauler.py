import requests


class Crauler:
    def __init__(self, config):
        self.config = config

    def __call__(self, url):
        return self.get_data(url)

    def get_data(self, url):
        r = requests.get(url)
        return r.text
