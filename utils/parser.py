import unidecode


class Parser:
    """
    parse news
    """

    def news(self, news: list) -> list:
        """
        method to parse a list of news
        """
        news_formatted = []

        for new in news:
            post_header = new.find("div", {"class": "post-header"})
            post_inner = new.find("div", {"class": "post-inner"})
            data_header = self.__format_header(post_header)
            data_inner = self.__format_inner(post_inner)

            news_formatted.append({
                **data_header,
                **data_inner
            })

        return news_formatted
    
    def __format_header(self, post_header):
        """
        format header of the news
        """
        title = post_header.find("h2", class_="bloco-title")
        autor = post_header.find("strong")
        date = post_header.find("div", class_="bloco-meta")

        data_header = {
            "title": self.__format_text(title),
            "autor": self.__format_text(autor),
            "date": self.__format_text(date)
        }

        return data_header
    

    def __format_inner(self, post_inner):
        """
        format inner of the news
        """
        text = ''
        p_tags = post_inner.find_all("p")
        for p in p_tags:
            text += self.__format_text(p)
        data_inner = {
            "text": text
        }

        return data_inner

    def __format_text(self, text:str) -> str:
        #return str(text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        if not text:
            return ''
        return unidecode.unidecode(text.text)
