import codecs
import os
from urllib.parse import urlparse


class Saver:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def escape(name):
        return name

    def make_path_by_url(self, url, ext='txt'):
        url = urlparse(url)
        dirs = [url.netloc] + [self.escape(p) for p in url.path.split('/') if p]
        file_name = dirs.pop()
        dir = '.'
        for d in dirs:
            dir = os.path.join(dir, d)
            if not os.path.exists(dir):
                os.mkdir(dir)
        file_name = f'{file_name}.{ext}'
        return os.path.join(dir, file_name)

    def save(self, text, path=None):
        file_path = self.make_path_by_url(path, 'txt')
        with codecs.open(file_path, 'w', 'utf_8_sig') as f:
            f.writelines(text)

    def dump(self, data, path=None):
        if not self.config['dump_original']:
            return
        file_path = self.make_path_by_url(path, 'html')
        with codecs.open(file_path, 'w', 'utf_8_sig') as f:
            f.writelines(data)
