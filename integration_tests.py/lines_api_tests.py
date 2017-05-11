import unittest
import requests
from config import Config


class LinesApiTests(unittest.TestCase):

    def setUp(self):
        self.lines_url = 'http://{}:{}/lines/'.format(
            Config.API_HOST,
            Config.API_PORT
        )

    def test_valid_line(self):
        resp = requests.get(self.lines_url + '1')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('price.ZECXBT', resp.text)

    def test_413_error(self):
        resp = requests.get(self.lines_url + '101')
        self.assertEqual(resp.status_code, 413)
        data = resp.json()
        self.assertEqual(data['error'], 'IndexOutOfRangeException')
