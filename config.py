import os
import logging

BASE_DIR = os.path.dirname(__file__)


def init_config():
    logging.basicConfig(
        format='%(asctime)-15s %(levelname)s %(message)s',
        level=logging.DEBUG)


class Config(object):

    DB_PATH = os.path.join(BASE_DIR, 'db', 'lineserver.db')

    API_HOST = '0.0.0.0'
    API_PORT = 8001

    CACHE_SIZE = 1  # In GB
