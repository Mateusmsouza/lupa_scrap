class Parser:
    """
    parse news
    """

    def news(self, news: list) -> list:
        """
        method to parse a list of news
        """
        for new in news:
            post_header = new.find("div", {"class": "post-header"})
            post_inner = new.find("div", {"class": "post-inner"})
            print(post_header)