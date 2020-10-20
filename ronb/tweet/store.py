from ronb.tweet.get import latest_tweets
from ronb.models import Tweet, Info, session


def store_info(tweet_count):
    tweet = session.query(Tweet).order_by(Tweet.timestamp.desc()).first()
    if tweet:
        this_info = Info(
            last_tweet_id=tweet.tweet_id,
            tweets_added=tweet_count
        )
        session.add(this_info)
        session.commit()


def last_tweet_id():
    info = session.query(Info).order_by(Info.last_checked.desc()).first()
    if info:
        return info.last_tweet_id


def add_tweet():
    added_tweet_count = 0
    for the_tweet in latest_tweets():
        the_tweet_id = session.query(Tweet).filter(
            Tweet.tweet_id == the_tweet['tweet_id']).first()
        if not the_tweet_id:
            this_tweet = Tweet(
                tweet_id=the_tweet['tweet_id'],
                timestamp=the_tweet['timestamp'],
                image_url=the_tweet['image_url'],
                tweet=the_tweet['tweet']
            )
            added_tweet_count += 1
            session.add(this_tweet)
    session.commit()
    store_info(added_tweet_count)
    return f"Added {added_tweet_count} new tweets!"
