import os
import sys
import argparse
from config import init_config
from db.lines_repository import LinesRepository


def main(args):
    init_config()
    if not os.path.exists(args.file):
        print('File path is invalid')
        sys.exit(1)

    LinesRepository().process_file(args.file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    main(args)
