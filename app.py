from flask import Flask
from telegram.ext import CommandHandler, Updater
from ronb.bot.main import the_tweeter
from os import environ

token = environ.get('BOT_TOKEN')
channel_name = environ.get('CHANNEL')
port = int(environ.get('PORT', 5000))
name = "ronbupdates"
host = "0.0.0.0"
url = f"https://{name}.now.sh"
updater = Updater(token, use_context=True)


app = Flask(__name__)


@app.route(f'/{token}', methods=['POST'])
def start():
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", the_tweeter))

    updater.idle()


@app.route('/webhook', methods=['GET', 'POST'])
def set_webhook():
    updater.start_webhook(listen=host, port=port, url_path=token)
    updater.bot.setWebhook(f'{url}/{token}')


@app.route('/')
def index():
    return 'Hello From Flask!'


if __name__ == '__main__':
    app.run(threaded=True)
