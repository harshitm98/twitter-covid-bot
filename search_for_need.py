import tweepy
from auth import authenticate, authenticate_search, authenticate_another
import requests
from config import FIREBASE_URL, FIREBASE_REPLIED_URL, FIREBASE_NEW_REPLIED_URL, FIREBASE_NEW_URL
import json
from dateutil.parser import parse
from add_to_db import upload_replied, get_database, if_already_replied
from time import sleep

with open("cities", "r") as f:
    cities = f.read().split("\n")
    cities = cities[:30]

keywords = ['oxygen', 'remdesivir', 'icu', 'hospital beds', 'plasma', 'ventilator'] 
search_keyword = "required OR leads"
ignore_bots = "-ShariqueAly -findthecolors"
filter_retweets = "-filter:retweets"

auth_search = authenticate_search()
api_search = tweepy.API(auth_search, wait_on_rate_limit=True)

auth_reply = authenticate()
api_reply = tweepy.API(auth_reply, wait_on_rate_limit=True)

auth_reply_1 = authenticate_another()
api_reply_1 = tweepy.API(auth_reply_1, wait_on_rate_limit=True)   

replied_in_this_session = []

replied_count = 0
for city in cities:
    
    print("[*] Searching for people in help in {}".format(city))
    for keyword in keywords:
        query = city + " " + keyword + " " + search_keyword + " " + ignore_bots
        tweets = api_search.search(query, count=100, result_type = "recent")
        available_data = get_database(city, keyword)
        for tweet in tweets:
            if "retweeted_status" not in tweet._json.keys():
                tweet_id = tweet._json["id"]
                if if_already_replied(str(tweet_id)) or str(tweet_id) in replied_in_this_session:
                    continue
                tweet_text = tweet._json["text"]
                tweet_time = tweet._json["created_at"]
                print("[-] Found a tweet with tweet id: {}".format(tweet_id), end=" -> ")
                reply_string = ""
                reply_string += "Here's a list of recent resources based on your keywords:\r\n"   
                count = 0
                for found_tweet in available_data:
                    if count >= 5:
                        break
                    if keyword == "plasma" and count == 4:
                        reply_string += "Find more donors at http://friends2support.org\r\n"
                    reply_string += found_tweet["tweet_link"] + "\r\n"
                    count += 1
                # twitter_query = "https://twitter.com/search?q=" + city + "+verified+" + keyword + "+-needed+-required+-leads&f=live" 
                if count == 0:
                    print("No leads found for {}.".format(keyword))
                    continue
                reply_string += "Find more resources at http://resourcesbot.surge.sh"
                print("Reply string: \n{}".format(reply_string))
                try:
                    if replied_count % 2 == 0:
                        api_reply.update_status(status = reply_string, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)
                        replied_count += 1
                    else:
                        api_reply_1.update_status(status = reply_string, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)                    
                        replied_count += 1
                except tweepy.error.TweepError as e:
                    print("TweepError: " + str(e))
                    if "185" in str(e):
                        sleep(600)
                        if replied_count % 2 == 0:
                            api_reply.update_status(status = reply_string, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)
                            replied_count += 1
                        else:
                            api_reply_1.update_status(status = reply_string, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)                    
                            replied_count += 1
                    if "281" in str(e):
                        print("API exhausted! Exiting the program!")
                        exit()             
                upload_replied(tweet_id)
                replied_in_this_session.append(str(tweet_id))
                sleep(20)