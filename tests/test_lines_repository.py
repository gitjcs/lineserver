import os
import unittest
from db.lines_repository import LinesRepository
from app.exceptions import IndexOutOfRangeException
from app.managers.lines_manager import LinesManager

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')


class LineRepositoryTests(unittest.TestCase):
    """
    We can do this as a unit test given were using sqlite as the db.
    for any other DB this is more of an integration test
    """

    def setUp(self):
        self.file_path = os.path.join(BASE_DIR, 'data', 'bitmex_zecxbt.csv')
        self.lines_repo = LinesRepository()

    def _process_file(self):
        cnt = self.lines_repo.process_file(self.file_path)
        self.assertEqual(cnt, 100)

    def test_process_file(self):
        self._process_file()

    def test_get_line(self):
        self._process_file()
        # Line 1 should be the header
        fisrt_line = self.lines_repo.get_line(1)
        self.assertTrue('price.ZECXBT' in fisrt_line)

        # Last line should be 100
        line = self.lines_repo.get_line(100)
        self.assertEqual(
            line,
            '"0.054971",".ZECXBT","2017-05-11T02:23:00.000Z"\n'
        )

    def test_out_of_range(self):
        self._process_file()
        # Out of range indexes
        with self.assertRaises(IndexOutOfRangeException):
            print(self.lines_repo.get_line(0))

        with self.assertRaises(IndexOutOfRangeException):
            print(self.lines_repo.get_line(-1))

        with self.assertRaises(IndexOutOfRangeException):
            print(self.lines_repo.get_line(101))

    def test_lines_manager(self):
        # Test the caching of lines managers
        self._process_file()
        manager = LinesManager()

        line1a = manager.get_line(1)

        # Getting the same line again should return the same object
        line1b = manager.get_line(1)
        self.assertIs(line1b, line1a)

        # If we clear the cache, well get a new object from the db
        manager.cache.clear()

        line1c = manager.get_line(1)
        self.assertIsNot(line1c, line1a)
