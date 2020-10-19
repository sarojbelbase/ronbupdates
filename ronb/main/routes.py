from flask import Blueprint
from ronb.utils.get_from_db import fetch_tweets

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return fetch_tweets()
