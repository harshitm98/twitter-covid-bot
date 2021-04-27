from config import consumer_key, consumer_secret, access_token, access_secret
from config import consumer_key_, consumer_secret_, access_token_, access_secret_
from config import consumer_key_1, consumer_secret_1, access_token_1, access_secret_1

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