from config import consumer_key, consumer_secret, access_token, access_secret
from config import consumer_key_, consumer_secret_, access_token_, access_secret_
from config import consumer_key_1, consumer_secret_1, access_token_1, access_secret_1
from config import MONGO_USERNAME, MONGO_PASSWORD
from pymongo import MongoClient

import tweepy

def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def authenticate_search():
    auth = tweepy.OAuthHandler(consumer_key_, consumer_secret_)
    auth.set_access_token(access_token_, access_secret_)
    return auth

def authenticate_another():
    auth = tweepy.OAuthHandler(consumer_key_1, consumer_secret_1)
    auth.set_access_token(access_token_1, access_secret_1)
    return auth

def get_collection(collection_name):
    connection_url = "mongodb+srv://{}:{}@cluster0.h2ugs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(MONGO_USERNAME, MONGO_PASSWORD)
    cluster = MongoClient(connection_url)
    db = cluster["tweet"]
    collection = db[collection_name]
    return collection