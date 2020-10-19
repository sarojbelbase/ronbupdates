from ronb.models import Tweet, session


def fetch_tweets():
    return session.query(Tweet).order_by(Tweet.timestamp.desc()).first()
