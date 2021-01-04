import logging
import re

from bs4 import BeautifulSoup

FAKE_TAGS = ["FALSO", "INSUSTENTÁVEL", "SUBESTIMADO", "CONTRADITÓRIO"]


class Analyzer:
    """
    Analyzes news
    """

    def analyze_news(self, soup_news) -> list:
        """
        analyze the soup news
        """
        logging.info("analyzing news collected")
        analyzed_news = []
        for news in soup_news:
            main_column = news.find("div", {"class": "column size-3-4 column-main"})
            tag_list = main_column.find_all("div", {"class": re.compile(r"etiqueta etiqueta-[0-9]")})
            fake = self.__is_fake(tag_list)
            if fake:
                analyzed_news.append(main_column)

        return analyzed_news
    
    def __is_fake(self, tag_list) -> bool:
        """
        validate if a news is fake or not
        """
        tag_list = list(set([tag.text for tag in tag_list]))

        if tag_list and tag_list.pop() in FAKE_TAGS:
            logging.debug("fake news found")
            return True
        
        logging.debug("fake news not found")
        return False