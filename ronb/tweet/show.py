from ronb.models import Tweet, Info, session


def logs():
    """ Expect to get tweets_added, last_tweet_id, last_checked. """
    return session.query(Info).order_by(Info.last_checked.desc()).first()


def fetch_tweets():
    return session.query(Tweet).order_by(Tweet.timestamp.desc()).all()
