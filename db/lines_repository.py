import logging
import time
from db import get_db

_logger = logging.getLogger(__name__)


class LinesRepository(object):

    def __init__(self):
        self.db = get_db()

    def process_file(self, filepath):
        cursor = self.db.cursor()
        # Not the most efficient thing here.
        # Using a migration tool like yoyo-migrations to only create the table
        # once and then just truncate on update would be better
        cursor.execute('''
            DROP TABLE IF EXISTS lines;
        ''')
        cursor.execute('''
            CREATE TABLE lines(line TEXT);
        ''')
        self.db.commit()

        ts = time.time()
        last_show = 0
        _logger.info('Processing: %s' % filepath)
        with open(filepath, 'r') as f:
            cnt = 0
            for line in f:
                # We could probably optimize this insert a bit more
                # but given the direction that "every line will fit in mem"
                # this is being safe and handling them one at a time
                cursor.execute('''
                    INSERT INTO lines VALUES (?)
                ''', (line,))
                self.db.commit()
                cnt += 1
                # Display speed every 2s
                te = time.time()
                if te - last_show > 2:
                    last_show = te
                    _logger.info('inserted {} lines in {:.1f}s'.format(
                        cnt, te - ts))

    def get_line(self, idx):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT line FROM lines
            WHERE rowid = ?
        ''', (idx,))

        data = cursor.fetchall()[0][0]
        return data
