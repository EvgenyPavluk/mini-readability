import json


class Config:
    DEFAULT_PARTS = ['crauler', 'extractor', 'formatter', 'saver']

    def __init__(self, config_name):
        self.config_name = config_name
        self.config = {}

    def __getattr__(self, name):
        if name not in self.config:
            raise Exception(f'Config has no {name} part')
        return self.config[name]

    def validate(self, config):
        for name in self.DEFAULT_PARTS:
            if name not in config:
                raise Exception(f'Config has no {name} part')

    def load(self):
        with open(self.config_name) as f:
            config = json.load(f)
        self.validate(config)
        self.config = config
