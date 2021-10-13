from clients.twitter.api import Twitter
from service.updater.tweet_updater import TweetUpdater, tweet_db, short_db
from service.parser.alexa_play import Parser
from service.search.youtube_search import YoutubeSearch, YoutubeVideo

def update():
    t = Twitter()
    tweets = t.search_paginated("alexa play")
    short_tweets = {}
    for tweet in tweets:
        short_tweets[tweet] = {
            "text": tweets[tweet]["text"]
            }
    u = TweetUpdater()
    u.update_db(tweets, tweet_db)
    u.update_db(short_tweets, short_db)
    fdb = u.get_tweets(tweet_db)
    sdb = u.get_tweets(short_db)
    print(len(fdb), len(sdb))


def process():
    u = TweetUpdater()
    fdb = u.get_tweets(tweet_db)
    sdb = u.get_tweets(short_db)
    
    print(len(fdb), len(sdb))
    psr = Parser()
    hapi = []
    rt = []
    inv = []
    for t in sdb:
        og = t['tweet']['text']
        
        if psr.is_retweet(og):
            rt.append(og)
        elif psr.is_valid_tweet(og):
            hapi.append(t)
            # print("-"*20)
            # print(og)
            # print("^^")
            psr_og = psr.parse(og)
            # print(psr_og)
            # print(f"song_name={psr.get_song_name(psr_og)}")
            # print(f"artist_name={psr.get_singer(psr_og)}")
        else:
            inv.append(og)
    # print(*rt, sep="\n->")
    print(f"og={len(sdb)} hapi={len(hapi)} rt={len(rt)} inv={len(inv)} t={len(hapi)+len(rt)+len(inv)}")
    # print(*inv, sep="\n->")
    
    for tweet_dict in hapi:
        tweet_text = tweet_dict['tweet']['text']
        tweet = psr.parse(tweet_text)
        song = psr.get_song_name(tweet)
        artist = psr.get_singer(tweet)
        
        ys = YoutubeSearch()
        ytv: YoutubeVideo = ys.get_famous_youtube_video(song, artist)
        print(ytv)
        print(tweet_text)
        print(ytv.title)
        print(ytv.viewCount["text"])
        print(ytv.link)
        print("-"*20)
        break
    
    

if __name__ == '__main__':
    import sys
    sys.path.append(".")
    
    # update()
    process()
    
    
    
    
    
    