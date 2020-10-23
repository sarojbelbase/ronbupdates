from ronb.models import Tweet, Info


def logs():
    """ Expect to get tweets_added, last_tweet_id, last_checked. """
    return Info.query.order_by(Info.last_checked.desc()).first()


def fetch_tweets():
    return Tweet.query.order_by(Tweet.timestamp.desc()).all()
