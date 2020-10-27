from ronb.models import Tweet, Info

# returns logs created by the database
def logs():
    """ Column names : tweets_added, last_tweet_id, last_checked. """
    return Info.query.order_by(Info.last_checked.desc()).first()


def fetch_tweets():
    return Tweet.query.order_by(Tweet.timestamp.desc()).all()
