import requests
from os import environ
from urllib.parse import urlencode
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
token = environ.get('BOT_TOKEN')
the_url = f"https://api.telegram.org/bot{token}/"
channel_name = environ.get('CHANNEL')
port = int(environ.get('PORT', 5000))
name = "ronbupdates"
host = "0.0.0.0"


def handle_error(the_url):
    try:
        response = requests.post(the_url)
        response.raise_for_status()
        return print(response.content.decode())
    except requests.exceptions.HTTPError as error:
        return print(error.response.text)


def send_message(message):
    send_url = 'sendMessage?'
    the_params = {
        'chat_id': channel_name,
        'text': message,
        'parse_mode': 'HTML'
    }
    message_url = the_url + send_url + urlencode(the_params)
    return handle_error(message_url)


def send_photo(image_url, caption):
    send_url = 'sendPhoto?'
    the_params = {
        'chat_id': channel_name,
        'photo': image_url,
        'caption': caption,
        'parse_mode': 'HTML'
    }
    photo_url = the_url + send_url + urlencode(the_params)
    return handle_error(photo_url)


def webhook_info(base_url):
    send_url = 'getWebhookInfo'
    main_url = base_url + send_url
    return handle_error(main_url)


def set_webhook(base_url):
    send_url = 'setWebhook'
    main_url = base_url + send_url
    return handle_error(main_url)


def delete_webhook(base_url):
    send_url = 'deleteWebhook'
    main_url = base_url + send_url
    return handle_error(main_url)
