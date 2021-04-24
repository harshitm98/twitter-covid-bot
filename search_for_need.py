import tweepy
from auth import authenticate, authenticate_search
import requests
from config import FIREBASE_URL, FIREBASE_REPLIED_URL
import json
from dateutil.parser import parse
from add_to_db import upload_replied

with open("cities", "r") as f:
    cities = f.read().split("\n")

keywords = ['oxygen', 'remdesiver', 'icu', 'hospital beds', 'plasma'] 
search_keyword = ['required', 'leads']

auth_search = authenticate_search()
api_search = tweepy.API(auth_search, wait_on_rate_limit=True)

auth_reply = authenticate()
api_reply = tweepy.API(auth_reply, wait_on_rate_limit=True)

def fetch_database():
    r = requests.get(FIREBASE_URL)
    if r.status_code != 200:
        print("Error fetching database!")
        return
    database = json.loads(r.text)
    print("[*] Database fetched!")
    return database    


def query_database(database,city, keywords, time):
    list_of_link = {}
    for key in database.keys():
        if database[key]["location"] == city:
            for keyword in keywords:
                if keyword in database[key]["keywords"]:
                    list_of_link[parse(database[key]["time"])] = database[key]["tweet_link"]
                    break
    return list_of_link

def get_already_replied_tweets():
    r = requests.get(FIREBASE_REPLIED_URL)
    replied = json.loads(r.text)
    print("[*] Fetched database of replied tweets!")
    if replied == None:
        return []
    return list(replied.values())
                
database = fetch_database()
already_replied_to_tweets = get_already_replied_tweets()
print(already_replied_to_tweets)

for city in cities:
    print("[*] Searching for people in help in {}".format(city))
    for keyword in keywords:
        # query = city + " " + keyword + " "  + " ".join(search_keyword)
        test_query = "Mumbai required oxygen " + "thisisatestforabotimcreatingpls"
        tweets = api_search.search(test_query, count=100)
        for tweet in tweets:
            found_keywords = []
            tweet_id = tweet._json["id"]
            if str(tweet_id) in already_replied_to_tweets:
                continue
            tweet_text = tweet._json["text"]
            tweet_time = tweet._json["created_at"]
            print("[-] Found a tweet with tweet id: {}\tText: {}".format(tweet_id, tweet_text))
            for all_keyword in keywords:
                if all_keyword in tweet_text.lower():
                    found_keywords.append(all_keyword)
                    print("Found {}".format(all_keyword))
                    
            print(found_keywords)
            list_of_available_links = query_database(database, city, found_keywords, tweet_time)
            list_of_keys = list(list_of_available_links.keys())
            list_of_keys.sort()
            list_of_keys.reverse()
            reply_string = ""
            reply_string += "Here's a list of recent tweets based on your keywords:\r\n"  
            for i in range(0, 5):
                reply_string += list_of_available_links[list_of_keys[i]] + "\r\n"
            # api_reply.update_status(status = reply_string, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)
            # upload_replied(tweet_id)
        break
    break
                    
        
        
             
    