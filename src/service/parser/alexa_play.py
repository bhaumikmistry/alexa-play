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
    
    def get_separater(self, text):
        if text.lower().find(" by ") != -1:
            return " by "
        elif text.lower().find(" from ") != -1:
            return " from "
        return ""
    
    def get_song_name(self, text):
        sep = self.get_separater(text)
        song = re.search('%s(.*)%s' % ("play", sep), text.lower())
        if song:
            return song.group(1)
        return None
    
    def get_singer(self, text):
        sep = self.get_separater(text)
        if sep is "":
            return ""
        last_part = text.lower().split(sep,1)[1]
        if len(last_part.split()) > 3:
            return " ".join(last_part.split()[0:3])
        else:
            return last_part
    
    def parse(self, text):
        text = self.remove_URL(text)
        text = self.remove_punctuation(text)
        return text
        
        