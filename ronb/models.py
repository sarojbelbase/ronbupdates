from os import environ
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

load_dotenv(find_dotenv())
engine = create_engine(environ.get('DATABASE_URL'))
session = Session(bind=engine)
BaseModel = declarative_base()


class Tweet(BaseModel):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    tweet_id = Column(BigInteger())
    timestamp = Column(DateTime())
    image_url = Column(String())
    tweet = Column(String())

    def __repr__(self):
        return f"Tweet{self.id}: [{self.tweet}]"
