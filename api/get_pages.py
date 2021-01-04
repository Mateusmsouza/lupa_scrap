import logging

import requests

class Requester:

    def get_page(self, url: str):
        logging.info(f'getting page {url}...')
        page = requests.get(url)
        return page
