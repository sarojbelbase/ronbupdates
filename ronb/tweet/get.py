# Ideas taken from https://gist.github.com/yanofsky/5436496

import re
import pytz
import tweepy
from os import environ
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


def latest_tweets(screen_name=environ.get('TWEETARATI')):

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(
        environ.get('CONSUMER_KEY'),
        environ.get('CONSUMER_SECRET')
    )
    auth.set_access_token(
        environ.get('ACCESS_KEY'),
        environ.get('ACCESS_SECRET')
    )
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(
        screen_name=screen_name,
        include_rts=False,
        exclude_replies=True,
        tweet_mode='extended')

    # save most recent tweets
    alltweets.extend(new_tweets)

    # beautified stuffs
    bleached_tweets = []
    for tweet in alltweets:
        try:
            # not all tweets will have media_url, so rain-checking
            image_url = tweet.entities['media'][0]['media_url']

        except (NameError, KeyError):
            # adding "None" with no image links
            bleached_tweets.append(save_this_one(tweet, "None"))
        else:
            # adding image_url for tweets that has image_links
            bleached_tweets.append(save_this_one(tweet, image_url))

    return bleached_tweets


def save_this_one(the_tweet, image):
    this_tweet = {
        "tweet_id": the_tweet.id_str,
        "timestamp": make_it_utc(the_tweet.created_at),
        "tweet": remove_url(the_tweet.full_text),
        "image_url": image
    }
    return this_tweet


def remove_url(text):
    modified = re.sub(r"http\S+", "", text)
    again = re.sub(r"[+]", "", modified)
    return again.encode("utf-8").decode("utf-8")


def make_it_utc(datetime_obj):
    return datetime_obj.replace(tzinfo=pytz.UTC)
