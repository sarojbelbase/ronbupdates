import logging
from os import environ
from dotenv import find_dotenv, load_dotenv
from telegram.ext import CommandHandler, Updater
from ronb.tweet.show import fetch_tweets

load_dotenv(find_dotenv())

token = environ.get('BOT_TOKEN')
channel_name = environ.get('CHANNEL')


# Enable logging
logging.basicConfig(
    format='%(levelname)s :  [ %(asctime)s ] - %(name)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def the_decider(context, the_list=fetch_tweets()):
    job = context.job
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
        the_decider, interval=30,  first=0, context=chat_id, name=str(chat_id))
    update.message.reply_text("Posted!")


def start():
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", the_tweeter))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
