import tweepy
import requests
from auth import authenticate, authenticate_another, authenticate_search
from add_to_db import get_database

with open("cities", "r+") as f:
    cities = f.read().split("\n")
    cities = cities[:30]

keywords = ['plasma', 'ventilator', 'remdesivir', 'icu', 'hospital beds', 'oxygen']

auth_reply = authenticate_another()
api_reply = tweepy.API(auth_reply, wait_on_rate_limit=True)

def get_mentions(api, since_id=0):
    # new_since_id = since_id
    tweets = api_reply.mentions_timeline(tweet_mode="extended")
    for tweet in tweets:
        print("Username: {}".format(tweet.user.screen_name))
        print("Tweet id: {}".format(tweet.id))
        print("Tweet text: {}".format(tweet.full_text))
        for city in cities:
            if city in tweet.full_text:
                for keyword in keywords:
                    if keyword in tweet.full_text:
                        database = get_database(city, keyword)
                        break
                break
        try:
            print("In reply to id: {}".format(tweet.in_reply_to_status_id))
        except:
            n = 0
        print("***")
        
        
get_mentions(api_reply)