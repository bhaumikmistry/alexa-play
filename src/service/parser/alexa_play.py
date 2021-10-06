import re
import string
from mysutils.text import remove_urls


class Parser:
    def __init__(self):
        print("Parser.__init__()")
    
    def has_alexa_play(self, text):
        if text.lower().find("alexa") != -1 and text.lower().find("play") != -1:
            pos = [text.lower().index(word) for word in ["alexa", "play"]]
            return pos == sorted(pos)
        return False
    
    def has_song_singer_separator(self, text):
        return text.lower().find("by") != -1 or text.lower().find("from") != -1
    
    def remove_URL(self, text):
        """Remove URLs from a text string"""
        # return re.sub(r"http\S+", "", text)
        return remove_urls(text)
    
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def is_valid_tweet(self, text):
        return not self.is_retweet(text) and self.has_alexa_play(text) and self.has_song_singer_separator(text)
    
    def is_retweet(self, text):
        return text.startswith("RT")
    
    def get_song_name(self, text):
        sep = ""
        if text.lower().find(" by ") != -1:
            sep = " by "
        elif text.lower().find(" from ") != -1:
            sep = " from "
        song = re.search('%s(.*)%s' % ("play", sep), text.lower()).group(1)
        return song
    
    def parse(self, text):
        text = self.remove_URL(text)
        text = self.remove_punctuation(text)
        return text
        
        