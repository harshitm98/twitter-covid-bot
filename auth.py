from config import consumer_key, consumer_secret, access_token, access_secret
import tweepy

def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
