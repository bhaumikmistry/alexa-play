from clients.twitter.api import Twitter
from service.updater.tweet_updater import TweetUpdater, tweet_db, short_db
from service.parser.alexa_play import Parser

if __name__ == '__main__':
    import sys
    sys.path.append(".")
    
    # t = Twitter()
    # tweets = t.search_paginated("alexa play")
    # short_tweets = {}
    # for tweet in tweets:
    #     short_tweets[tweet] = {
    #         "text": tweets[tweet]["text"]
    #         }
    u = TweetUpdater()
    # u.update_db(tweets, tweet_db)
    # u.update_db(short_tweets, short_db)
    fdb = u.get_tweets(tweet_db)
    sdb = u.get_tweets(short_db)
    print(len(fdb), len(sdb))
    
    psr = Parser()
    hapi = 0
    for t in sdb:
        og = t['tweet']['text']
        if psr.has_alexa_play(og):
            hapi+=1
            print("-"*20)
            print(og)
            print("^^")
            print(psr.parse(og))
print(f"og={len(sdb)} hapi={hapi}")
    
    
    
    