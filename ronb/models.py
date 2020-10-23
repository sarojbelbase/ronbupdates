# OLD VERSION AVAILABLE AT | https://gist.github.com/383744970eb684941b314e95667c37bd

from ronb import db
from datetime import datetime


class Tweet(db.Model):
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    image_url = db.Column(db.String)
    tweet = db.Column(db.String)

    def __repr__(self):
        return f"Tweet{self.id}: [{self.tweet}]"


class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    last_checked = db.Column(db.DateTime, default=datetime.utcnow)
    last_tweet_id = db.Column(db.String)
    tweets_added = db.Column(db.Integer)

    def __repr__(self):
        return f"Added {self.tweets_added} new tweets on {self.last_checked} with last tweet_id : {self.last_tweet_id}"
