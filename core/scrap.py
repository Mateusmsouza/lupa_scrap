import logging
import math
import re

from bs4 import BeautifulSoup
from bs4.element import Tag

from api.get_pages import Requester
from core.analyzer import Analyzer
from utils.parser import Parser

MONTHS = [
    {
        "date" : "2020/12",
        "news_quantity": 59
    },
    {
        "date": "2020/11",
        "news_quantity": 244
    },
    {
        "date": "2020/10",
        "news_quantity": 168
    },
    {
        "date": "2020/09",
        "news_quantity": 88
    },
    {
        "date": "2020/08",
        "news_quantity": 109
    },
    {
        "date": "2020/07",
        "news_quantity": 130
    },
    {
        "date": "2020/06",
        "news_quantity": 181
    },
    {
        "date": "2020/05",
        "news_quantity": 175
    },
    {
        "date": "2020/04",
        "news_quantity": 169
    },
    {
        "date": "2020/03",
        "news_quantity": 89
    },
    {
        "date": "2020/02",
        "news_quantity": 50
    },
    {
        "date": "2020/01",
        "news_quantity": 56
    }
]
BASE_URL = "https://piaui.folha.uol.com.br/lupa"


class JournalScrap:

    def start_scrap(self):
        logging.info("starting scrapping on lupa")
        #urls = self.__create_urls()
        # for url in urls:
        #     page = Requester().get_page(url)
        #     logging.debug(page)
        page = Requester().get_page("https://piaui.folha.uol.com.br/lupa/2020/12/page/3/")
        soup = BeautifulSoup(page.text, 'html.parser')

        news_div = soup.findAll("div", {"class": "internaPGN"})
        
        soup_news = []
        for news_preview in news_div[0]:
            if isinstance(news_preview, Tag):
                page = Requester().get_page(news_preview.a["href"])
                soup_news.append(BeautifulSoup(page.text, 'html.parser'))
        
        # analyzing and parsing the data here
        news_analyzed = Analyzer().analyze_news(soup_news)
        news_analyzed = Parser().news(news_analyzed)
        

                

    def __create_urls(self):
        logging.debug("creating urls")

        urls = []
        for month in MONTHS:
            page_numbers = math.ceil(
               month["news_quantity"]/10)

            for page in range(page_numbers):
                urls.append(
                    f'{BASE_URL}/{month["date"]}/page/{page}'
                )

        return urls
