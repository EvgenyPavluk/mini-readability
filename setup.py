#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Mini_readability',
    version='1.0',
    description='HTML text extractor and formatter',
    author='Evgeny Pavlyuk',
    author_email='ephouse@yandex.ru',
    install_requires=["lxml", "pytest", "requests"]
)