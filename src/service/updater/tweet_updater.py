#/usr/bin/python3
from clients.twitter.api import Twitter
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

# with open("data_file.json", "w") as f:
#     json.dump(data, f)

tweet_db = TinyDB('tweets.json', sort_keys=True, indent=4, separators=(',', ': '), storage=CachingMiddleware(JSONStorage))
short_db = TinyDB('short_tweets.json', sort_keys=True, indent=4, separators=(',', ': '), storage=CachingMiddleware(JSONStorage))


class TweetUpdater:
    def __init__(self):
        print("Updater().init()")

    def update_db(self, tweets, db: TinyDB):
        for tweet in tweets:        
            data = {
                'id': tweet,
                'tweet': tweets[tweet]
            }
            if self.get_tweet(tweet, db):
                continue
            db.insert(data)
        db.close()
    
    def get_tweets(self, db: TinyDB):
        return db.all()
    
    def get_tweet(self, id, db: TinyDB):
        tweet = Query()
        return db.search(tweet.id == id)