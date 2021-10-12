from src.clients.youtube.api import Youtube

class YoutubeSearch:
    
    def __init__(self):
        self._api = Youtube()
        
    def get_famous_link(self, song_name, artist_name):
        searched_list = self._api.search()