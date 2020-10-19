from .get_tweets import those_tweets
from ronb.models import Tweet
from ronb import db


def add_tweet_to_db():
    added_tweet_count = 0
    for the_tweet in those_tweets():
        the_tweet_id = Tweet.filter_by(
            Tweet.tweet_id == the_tweet['tweet_id']).first()
        if not the_tweet_id:
            this_tweet = Tweet(
                tweet_id=the_tweet['tweet_id'],
                timestamp=the_tweet['timestamp'],
                image_url=the_tweet['image_url'],
                tweet=the_tweet['tweet']
            )
            added_tweet_count += 1
            db.add(this_tweet)
    db.commit()
    return f"Added {added_tweet_count} New Tweets!"


# print(add_tweet_to_db())
