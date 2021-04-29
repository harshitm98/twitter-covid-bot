import tweepy
import requests
from config import FIREBASE_NEW_URL, FIREBASE_REPLIED_URL, FIREBASE_NEW_REPLIED_URL
from auth import authenticate, authenticate_another, authenticate_search

auth_reply = authenticate()
api_reply = tweepy.API(auth_reply, wait_on_rate_limit=True)

def get_mentions(since_id=0):
    # new_since_id = since_id
    tweets = api_reply.mentions_timeline(tweet_mode="extended")
    for tweet in tweets:
        print("Username: {}".format(tweet.user.screen_name))
        print("Tweet id: {}".format(tweet.id))
        print("Tweet text: {}".format(tweet.full_text))
        try:
            print("In reply to id: {}".format(tweet.in_reply_to_status_id))
        except:
            n = 0
        print("***")
        
        
get_mentions()