from os import environ
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime

load_dotenv(find_dotenv())
engine = create_engine(environ.get('DATABASE_URL'),
                       connect_args={'check_same_thread': False})
session = Session(bind=engine)
BaseModel = declarative_base()


class Tweet(BaseModel):
    __tablename__ = 'tweet'
    id = Column(Integer(), primary_key=True)
    tweet_id = Column(String())
    timestamp = Column(DateTime())
    image_url = Column(String())
    tweet = Column(String())

    def __repr__(self):
        return f"Tweet{self.id}: [{self.tweet}]"


class Info(BaseModel):
    __tablename__ = 'info'
    id = Column(Integer(), primary_key=True)
    last_checked = Column(DateTime(), default=datetime.utcnow)
    last_tweet_id = Column(String())
    tweets_added = Column(Integer())

    def __repr__(self):
        return f"Added {self.tweets_added} new tweets on {self.last_checked} with last tweet_id : {self.last_tweet_id}"
