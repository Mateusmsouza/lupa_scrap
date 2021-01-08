import os
import json
import logging

PATH = "lupa_fake_news"
ACCESS_RIGHT = 0o755

class Saver:
    """
    Save news to files
    """
    
    def save(self, news: list):
        """
        save a list of news
        """
        logging.info("saving news...")
        try:
            logging.debug("trying to create dir to store news")
            os.mkdir(PATH, ACCESS_RIGHT)
        except FileExistsError:
            logging.debug("dir already exists.")
        

        for index, new in enumerate(news):
            with open(f'{PATH}/{index}.json', 'w') as fp:
                json.dump(new, fp)
        
        logging.info("saving completed")
        
