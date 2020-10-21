import logging
from os import environ
from dotenv import find_dotenv, load_dotenv
from telegram.ext import CommandHandler, Updater
from ronb.tweet.show import fetch_tweets, logs
from ronb.tweet.store import add_tweet

load_dotenv(find_dotenv())

token = environ.get('BOT_TOKEN')
channel_name = environ.get('CHANNEL')
port = int(environ.get('PORT', 5000))
name = "ronbupdates"
host = "0.0.0.0"

# # Enable logging
# logging.basicConfig(
#     format='%(levelname)s :  [ %(asctime)s ] - %(name)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)


def the_decider(context):
    add_tweet()
    job = context.job
    count = int(logs().tweets_added)
    the_list = fetch_tweets()[:count][::-1]
    for the_tweet in the_list:
        if the_tweet.image_url == "None":
            context.bot.send_message(job.context, text=the_tweet.tweet)
        else:
            context.bot.send_photo(
                job.context,
                photo=the_tweet.image_url,
                caption=the_tweet.tweet)


def the_tweeter(update, context):
    chat_id = channel_name
    context.job_queue.run_repeating(
        the_decider,
        interval=20,
        first=0,
        context=chat_id,
        name=str(chat_id)
    )
    update.message.reply_text("Incoming!")


# def start():
#     updater = Updater(token, use_context=True)

#     # Get the dispatcher to register handlers
#     dp = updater.dispatcher

#     # on different commands - answer in Telegram
#     dp.add_handler(CommandHandler("start", the_tweeter))

#     # Start the Bot

#     updater.start_polling()
#     # updater.start_webhook(listen=host, port=port, url_path=token)
#     # updater.bot.setWebhook(f"https://{name}.herokuapp.com/{token}")

#     # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
#     # SIGABRT. This should be used most of the time, since start_polling() is
#     # non-blocking and will stop the bot gracefully.
#     updater.idle()
