import re
import string
from mysutils.text import remove_urls


class Parser:
    def __init__(self):
        print("Parser.__init__()")
    
    def has_alexa_play(self, text):
        return text.lower().find("alexa") != -1 and text.lower().find("play") != -1
    
    def remove_URL(self, text):
        """Remove URLs from a text string"""
        # return re.sub(r"http\S+", "", text)
        return remove_urls(text)
    
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def parse(self, text):
        text = self.remove_URL(text)
        text = self.remove_punctuation(text)
        return text
        
        