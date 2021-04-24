import tweepy
from auth import authenticate, authenticate_search
import json
from add_to_db import upload_data
from tweet_entity import TweetEntity

with open("cities", "r") as f:
    cities = f.read().split("\n")

keywords = ['oxygen', 'remdesiver', 'icu', 'hospital beds']

auth = authenticate_search()
api = tweepy.API(auth, wait_on_rate_limit=True)

for city in cities:
    print("[*] Searching for resources in {}...".format(city))
    for keyword in keywords:
        print("\t Looking for {}...".format(keyword), end=" -> ")
        query = city + " " + keyword + " verified"
        tweets = api.search(query, count=1000)
        print("Found: {} tweets".format(len(tweets)))
        for tweet in tweets:
            found_additional_keywords = [keyword]
            if "retweeted_status" not in tweet._json.keys():
                tweet_id = tweet._json["id"]
                tweet_time = tweet._json["created_at"]
                tweet_text = tweet._json["text"]
                try:
                    tweet_link = tweet._json["entities"]["urls"][0]["expanded_url"]
                except:
                        tweet_username = tweet._json["user"]["screen_name"]
                        tweet_link = "https://twitter.com/" + tweet_username + "/status/" + str(tweet_id)
                for additional_keyword in keywords:
                    if additional_keyword in tweet_text and additional_keyword not in found_additional_keywords:
                        found_additional_keywords.append(additional_keyword)
                upload_data(TweetEntity(tweet_id, city, ", ".join(found_additional_keywords), tweet_link, tweet_time))