#!/usr/bin/env python
import argparse

from config import Config
from crauler import Crauler
from formatter import Formatter
from extractor import Extractor
from saver import Saver


def main(args):
    config = Config(args.config_name)
    config.load()
    crauler = Crauler(config.crauler)
    formatter = Formatter(config.formatter)
    extractor = Extractor(config.extractor)
    saver = Saver(config.saver)

    data = crauler(args.url)
    saver.dump(data, args.url)
    lines = extractor(data)
    text = formatter(lines)
    saver.save(text, args.url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get html by url and extract text data.')
    parser.add_argument('-c', '--config', dest='config_name', default='default.json',
                        help='config file name (default: "default.json")')
    parser.add_argument('-u', '--url', dest='url', default='https://lenta.ru/articles/2020/12/02/ad/',
                        help='url (default: "https://lenta.ru/articles/2020/12/02/ad/")')
    args = parser.parse_args()
    main(args)
