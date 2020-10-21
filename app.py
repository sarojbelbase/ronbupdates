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
    update = Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    bot.sendMessage(chat_id=channel_name, text="Hello!",
                    reply_to_message_id=msg_id)


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
