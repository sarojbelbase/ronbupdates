from flask import Flask
from ronb.tweet.show import fetch_tweets, logs
from ronb.tweet.store import add_tweet
from ronb.bot import send_message, send_photo, set_webhook, delete_webhook, get_webhook_info
from os import environ

name = "ronbupdates"
base_url = f"https://{name}.now.sh/"
token = environ.get('BOT_TOKEN')


app = Flask(__name__)


@app.route(f'/test', methods=['POST'])
def send_to_channel():
    add_tweet()
    set_webhook(base_url)
    count = int(logs().tweets_added)
    the_list = fetch_tweets()[:count][::-1]
    for the_tweet in the_list:
        if the_tweet.image_url == "None":
            send_message(the_tweet.tweet)
        else:
            send_photo(the_tweet.image_url, the_tweet.tweet)
    return "ok"


@app.route('/webhook/set', methods=['GET', 'POST'])
def webhook_set():
    delete_webhook(base_url)
    set_webhook(base_url)
    return "ok"


@app.route('/webhook/remove', methods=['GET', 'POST'])
def remove_webhook():
    delete_webhook(base_url)
    return "ok"


@app.route('/webhook/info', methods=['GET', 'POST'])
def webhook_info():
    get_webhook_info(base_url)
    return "ok"


@app.route('/')
def index():
    return 'Hello From Flask!'


if __name__ == '__main__':
    app.run(threaded=True)
