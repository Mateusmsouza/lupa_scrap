import logging

from core.scrap import JournalScrap

logging.basicConfig(format='%(levelname)s: %(message)s: %(filename)s: %(lineno)s', level=logging.DEBUG)


if __name__ == '__main__':
    JournalScrap().start_scrap()