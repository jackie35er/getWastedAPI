import configparser
import os


def setup():
    Config.load(os.path.join(os.path.dirname(__file__), 'resources', 'config.ini'))


class Config:
    __conf = {}

    @staticmethod
    def config(name):
        return Config.__conf[name]

    @staticmethod
    def load(file: str):
        config = configparser.ConfigParser()
        config.read(file)
        Config.__conf = config
