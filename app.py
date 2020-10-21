from flask import Flask, request
from telegram import Bot, Update
from ronb.tweet.show import fetch_tweets, logs
from ronb.tweet.store import add_tweet
from os import environ

token = environ.get('BOT_TOKEN')
channel_name = environ.get('CHANNEL')
port = int(environ.get('PORT', 5000))
name = "ronbupdates"
host = "0.0.0.0"
url = f"https://{name}.now.sh"
bot = Bot(token=token)


app = Flask(__name__)


@app.route(f'/{token}', methods=['POST'])
def send_to_channel():
    add_tweet()
    set_webhook()
    count = int(logs().tweets_added)
    the_list = fetch_tweets()[:count][::-1]
    for the_tweet in the_list:
        if the_tweet.image_url == "None":
            bot.send_message(channel_name, text=the_tweet.tweet)
        else:
            bot.send_photo(
                channel_name,
                photo=the_tweet.image_url,
                caption=the_tweet.tweet)
    return "Executed Sucessfully!"


@app.route('/webhook', methods=['GET', 'POST'])
def set_webhook():
    bot.delete_webhook()
    webhook = bot.set_webhook(f'{url}/{token}')
    if webhook:
        return "Webhook :)"
    else:
        return "Webhook :("


@app.route('/')
def index():
    return 'Hello From Flask!'


if __name__ == '__main__':
    app.run(threaded=True)
