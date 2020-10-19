from ronb import db


class Tweet(db.Model):
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.BigInteger())
    timestamp = db.Column(db.DateTime())
    image_url = db.Column(db.String())
    tweet = db.Column(db.String())

    def __repr__(self):
        return f"Tweet{self.id}: [{self.tweet}]"
