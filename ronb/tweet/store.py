from datetime import datetime
from ronb.tweet.get import latest_tweets
from ronb.models import Tweet, Info
from ronb import db


def update_log(tweet_count):
    tweet = Tweet.query.order_by(Tweet.timestamp.desc()).first()
    info = Info.query.get(1)
    if tweet and info:
        info.last_tweet_id = tweet.tweet_id
        info.tweets_added = tweet_count
        info.last_checked = datetime.utcnow()
        db.session.add(info)


def add_tweet():
    added_tweet_count = 0
    got_tweets = int(len(latest_tweets()))
    for the_tweet in latest_tweets():
        the_tweet_id = Tweet.query.filter(
            Tweet.tweet_id == the_tweet['tweet_id']).first()
        # If the tweet_id not already in db & if there are tweets to be fetched
        if not the_tweet_id and got_tweets > 0:
            this_tweet = Tweet(
                tweet_id=str(the_tweet['tweet_id']),
                timestamp=the_tweet['timestamp'],
                image_url=the_tweet['image_url'],
                tweet=the_tweet['tweet']
            )
            added_tweet_count += 1
            db.session.add(this_tweet)
            update_log(added_tweet_count)
    db.session.commit()
    return added_tweet_count
