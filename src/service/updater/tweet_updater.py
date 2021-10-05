#/usr/bin/python3
from clients.twitter.api import Twitter
from tinydb import TinyDB, Query

# with open("data_file.json", "w") as f:
#     json.dump(data, f)

tweet_db = TinyDB('tweets.json')
short_db = TinyDB('short_tweets.json')


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
    
    def get_tweets(self, db: TinyDB):
        return db.all()
    
    def get_tweet(self, id, db: TinyDB):
        tweet = Query()
        return db.search(tweet.id == id)