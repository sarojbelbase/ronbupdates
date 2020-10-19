from flask import render_template
from ronb.models import Tweet


def fetch_tweets():
    return Tweet.query.order_by(Tweet.timestamp.desc()).first()
