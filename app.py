from ronb.tweet.store import add_tweet
from ronb.tweet.show import fetch_tweets
from ronb.models import Tweet, Info, session
from ronb.bot.main import start

if __name__ == '__main__':
    start()
    # print(dir(session.query(Tweet)))
    # print(session.query(Info).all())
    # print(fetch_tweets())
    # print(add_tweet())
