import sys
from cachetools import LRUCache
from config import Config
from db.lines_repository import LinesRepository
from app.exceptions import IndexOutOfRangeException

GB_BYTES = 1024 * 1024 * 1024


class LinesManager(object):

    def __init__(self):
        self.cache = LRUCache(maxsize=Config.CACHE_SIZE * GB_BYTES,
                              getsizeof=sys.getsizeof)

    def get_line(self, line_idx):
        if line_idx < 1:
            raise IndexOutOfRangeException()

        try:
            return self.cache[line_idx]
        except KeyError:
            # Sqlite is weird with threading, need to create a new
            # connection per request. With a real db wed create one
            # connection in __init__ and reuse that
            line = LinesRepository().get_line(line_idx)
            try:
                self.cache[line_idx] = line
            except Exception:
                # we can get a ValueError if the size of line is greater
                # than the size of the cache. Catch all errors regardless,
                # Failure to cache is not critical
                pass

            return line
