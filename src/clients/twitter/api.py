#/usr/bin/python3
from TwitterAPI import TwitterAPI, HydrateType, TwitterPager, TwitterOAuth
import json
from .credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

QUERY = 'alexa play'
EXPANSIONS = 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,in_reply_to_user_id,attachments.media_keys'
MEDIA_FIELDS = 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics'
TWEET_FIELDS = 'created_at,author_id,public_metrics'
USER_FIELDS = 'location,profile_image_url,verified'

MIXED="mixed"
RECENT="recent"
POPULAR="popular"

class Twitter():
    def __init__(self):
        self._api = self._get_client()

    def _get_client(self):
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        return api

    def search(self, text, result_type=RECENT):
        r = self._api.request('search/tweets', 
            {
                'q':{'alexa play'},
                'count': 100,
                'result_type':RECENT,
                'tweet.fields': TWEET_FIELDS,
                'user.fields': USER_FIELDS,
		    })
        for item in r:
            tweet = json.dumps(item, indent=2)
        return r

    def search_paginated(self, text, tweet_per_call=100, tweet_count=500):
        pager = TwitterPager(self._api, 
            'search/tweets', 
            {
                'q':{text},
                'count': tweet_per_call,
                'result_type':RECENT,
                'tweet.fields': TWEET_FIELDS,
                'user.fields': USER_FIELDS,
		    }
        )

        count = 0
        data = {}
        for item in pager.get_iterator(wait=5):
            data[item["id"]]=item
            print("geting tweets . .", len(data))
            count+=1
            if count>=tweet_count:
                break
        return data
