# import csv
# import json
import re
import pytz
import tweepy
from flask import current_app


def those_tweets(screen_name=current_app.config['TWEETARATI']):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(
        current_app.config['CONSUMER_KEY'],
        current_app.config['CONSUMER_SECRET']
    )
    auth.set_access_token(

        current_app.config['ACCESS_KEY'],
        current_app.config['ACCESS_SECRET']
    )
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(
        screen_name=screen_name,
        count=1,
        include_rts=False,
        exclude_replies=True,
        tweet_mode='extended')

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=screen_name,
            count=200, max_id=oldest,
            include_rts=False,
            exclude_replies=True,
            tweet_mode='extended')

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f" Got {len(alltweets)} tweets so far...")

    bleached_tweets = []  # making proper headers
    for tweet in alltweets:
        try:
            # not all tweets will have media url, so rain-checking
            tweet.entities['media'][0]['media_url']

        except (NameError, KeyError):
            # adding "None" with no image links
            bleached_tweets.append(
                {
                    "tweet_id": tweet.id_str,
                    "timestamp": make_it_utc(tweet.created_at),
                    "tweet": remove_url(tweet.full_text),
                    "image_url": "None"
                }
            )
        else:
            # adding image_url for image_links
            bleached_tweets.append(
                {
                    "tweet_id": tweet.id_str,
                    "timestamp": make_it_utc(tweet.created_at),
                    "tweet": remove_url(tweet.full_text),
                    "image_url": tweet.entities['media'][0]['media_url']
                }
            )

    return bleached_tweets


def remove_url(text):
    modified = re.sub(r"http\S+", "", text)
    return modified.encode("utf-8").decode("utf-8")


def make_it_utc(datetime_obj):
    return datetime_obj.replace(tzinfo=pytz.UTC)

# If you want to store it as a csv
# def write_to_csv():
#     with open(f'{TWEETARATI}.csv', 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(["id", "timestamp", "tweet", "image_url"])
#         writer.writerows(those_tweets())

# If you want to store it as a json
# def write_to_json():
#     with open(f"{TWEETARATI}.json", "w", encoding='utf8') as file:
#         the_tweets = json.dumps(get_all_tweets(
#             TWEETARATI), indent=4, sort_keys=True, default=str, ensure_ascii=False)
#         file.write(the_tweets)

# Possible due to https://gist.github.com/yanofsky/5436496
