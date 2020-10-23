from ronb.bot import send_message, send_photo, set_webhook, delete_webhook, get_webhook_info
from ronb.tweet.store import add_tweet
from ronb.tweet.show import fetch_tweets, logs
from flask import render_template, Blueprint
from ronb.config import Configuration as creds

main = Blueprint('main', __name__)


name = "ronbupdates"
base_url = f"https://{name}.herokuapp.com/"
token = creds.BOT_TOKEN
secret = creds.SECRET_KEY


@main.route(f'/{secret}')
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


@main.route('/webhook/set', methods=['GET', 'POST'])
def webhook_set():
    delete_webhook(base_url)
    set_webhook(base_url)
    return "ok"


@main.route('/webhook/remove', methods=['GET', 'POST'])
def remove_webhook():
    delete_webhook(base_url)
    return "ok"


@main.route('/webhook/info', methods=['GET', 'POST'])
def webhook_info():
    get_webhook_info(base_url)
    return "ok"


@main.route('/')
def home():
    return render_template('home.html', tweets=fetch_tweets()[:3])
