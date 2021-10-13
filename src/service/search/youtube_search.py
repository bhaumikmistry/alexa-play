from clients.youtube.api import Youtube
from model.youtube_video import YoutubeVideo


class YoutubeSearch:
    
    def __init__(self):
        self._api = Youtube()
        
    def _get_views_in_number(self, str_view):
        number = str_view.split(' ')[0]
        print(number)
        number = int(number.replace(',', ''))
        print(number)
        return number
        
    def get_famous_youtube_video(self, song_name, artist_name) -> YoutubeVideo:
        print(f"looking for {song_name} by {artist_name}")
        searched_list = self._api.search(song_name, artist_name)
        famous_item_count = 0
        famous_item = None
        print(len(searched_list))
        for item in searched_list:
            item = YoutubeVideo(item)
            str_view = item.viewCount["text"]
            print(item.title)
            print(str_view)
            view = self._get_views_in_number(str_view)
            if view > famous_item_count:
                if song_name in item.title:
                    famous_item_count = view
                    famous_item = item
        print(famous_item_count)
        print(famous_item)
        return famous_item
    