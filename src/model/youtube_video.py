class YoutubeVideo:
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
        """
        {
            "type": "video",
            "id": "E07s5ZYygMg",
            "title": "Harry Styles - Watermelon Sugar (Official Video)",
            "publishedTime": "6 months ago",
            "duration": "3:09",
            "viewCount": {
                "text": "162,235,006 views",
                "short": "162M views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAOWBTE1SDrtrDQ1aWNzpDZ7YiMIw",
                    "width": 360,
                    "height": 202
                },
                {
                    "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD7U54pGZLPKTuMP-J3kpm4LIDPVg",
                    "width": 720,
                    "height": 404
                }
            ],
            "descriptionSnippet": [
                {
                    "text": "This video is dedicated to touching. Listen to Harry Styles' new album 'Fine Line' now: https://HStyles.lnk.to/FineLineAY Follow\u00a0..."
                }
            ],
            "channel": {
                "name": "Harry Styles",
                "id": "UCZFWPqqPkFlNwIxcpsLOwew",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GgNUvHxwlnz4RpHamcGnZF1px13VHj01TPksw=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UCZFWPqqPkFlNwIxcpsLOwew"
            },
            "accessibility": {
                "title": "Harry Styles - Watermelon Sugar (Official Video) by Harry Styles 6 months ago 3 minutes, 9 seconds 162,235,006 views",
                "duration": "3 minutes, 9 seconds"
            },
            "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
            "shelfTitle": null
        }
        """