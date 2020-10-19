from ronb.core.get_tweets import those_tweets
from ronb.models import Tweet, session


def add_tweet_to_db():
    added_tweet_count = 0
    for the_tweet in those_tweets():
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
    return f"Added {added_tweet_count} New Tweets!"


# print(add_tweet_to_db())
