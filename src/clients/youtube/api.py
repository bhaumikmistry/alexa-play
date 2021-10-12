from youtubesearchpython import VideosSearch
from typing import List


class Youtube:
    def __init__(self):
        self.query_count = 15
    
    def _make_query(self, song_name, artist_name):
        return f'{song_name} by {artist_name}'
    
    def search(self, song_name, artist_name) -> List:
        query = self._make_query(song_name, artist_name)
        videosSearch = VideosSearch(query, limit = self.query_count)
        return videosSearch.result()["result"]