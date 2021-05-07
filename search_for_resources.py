import tweepy
from auth import authenticate, authenticate_search
import json
from add_to_db import upload_data, is_exists_in_database
from tweet_entity import TweetEntity
import requests
import json
from time import sleep
import random
from dateutil.parser import parse

with open("cities", "r") as f:
    cities = f.read().split("\n")
    cities = cities[:30]


keywords = ['oxygen', 'remdesivir', 'icu', 'hospital beds', 'plasma', 'ventilator']
search_keyword = "verified"
ignore_keywords = "-needed -required -leads -requirement -need -please"
ignore_bots = "-ShariqueAly -findthecolors"
filter_out = "-filter:retweets"

auth = authenticate_search()
api = tweepy.API(auth, wait_on_rate_limit=True)

def create_data(tweet_entity):
    random_int = random.getrandbits(128)
    data_to_upload = {}
    data_to_upload["_id"] = str(random_int)
    data_to_upload["tweet_id"] = str(tweet_entity.tweet_id)
    data_to_upload["keywords"] = tweet_entity.keywords
    data_to_upload["location"] = tweet_entity.location
    data_to_upload["time"] = str(parse(tweet_entity.time))
    data_to_upload["tweet_link"] = tweet_entity.tweet_link
    data_to_upload["tweet_text"] = tweet_entity.tweet_text
    return data_to_upload


for city in cities:
    print("[*] Searching for resources in {}...".format(city))
    list_to_upload = []
    for keyword in keywords:
        old_tweets = 0
        retweets = 0
        print("\t Looking for {}...".format(keyword), end=" -> ")
        query = city + " " + keyword + " " + search_keyword + " " + ignore_keywords + " " + ignore_bots + " " + filter_out
        tweets = api.search(query, count=100, result_type = "recent", tweet_mode = "extended")
        print("Found: {} tweets".format(len(tweets)), end = " ")
        for tweet in tweets:
            found_additional_keywords = [keyword]
            if "retweeted_status" not in tweet._json.keys():
                tweet_id = tweet._json["id"]
                if is_exists_in_database(tweet_id):
                    old_tweets += 1
                    continue
                tweet_time = tweet._json["created_at"]
                tweet_text = tweet._json["full_text"]
                tweet_text = tweet_text.replace("\n", " ")
                tweet_username = tweet._json["user"]["screen_name"]
                tweet_link = "https://twitter.com/" + tweet_username + "/status/" + str(tweet_id)
                for additional_keyword in keywords:
                    if additional_keyword in tweet_text and additional_keyword not in found_additional_keywords:
                        found_additional_keywords.append(additional_keyword)
                list_to_upload.append(create_data(TweetEntity(tweet_id, city, ", ".join(found_additional_keywords), tweet_link, tweet_time, tweet_text)))
            else:
                retweets += 1
        print("-> New Tweets: {}".format(len(tweets) - old_tweets - retweets))
    if len(list_to_upload) == 0:
        continue
    upload_data(list_to_upload)