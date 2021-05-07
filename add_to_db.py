import requests
import random
import json
from tweet_entity import TweetEntity
from auth import get_collection


def upload_replied(tweet_id):
    random_int = random.getrandbits(128)
    data = {}
    data["_id"] = str(random_int)
    data["tweet_id"] = str(tweet_id)
    collection = get_collection("reply")
    collection.insert_one(data)
    print("Replied with resources!")
    

def upload_data(list_of_data):
    collection = get_collection("data")
    collection.insert_many(list_of_data)


def is_exists_in_database(tweet_id):
    collection = get_collection("data")
    if collection.find_one({"tweet_id": str(tweet_id)}) != None:
        return True
    return False


def get_database(city, keyword):
    collection = get_collection("data")
    query = {"location": city, "keywords": {"$regex": keyword}}
    database = collection.find(query).sort("time", -1)
    return database


def if_already_replied(tweet_id):
    collection = get_collection("reply")
    if collection.find_one({"tweet_id": str(tweet_id)}) != None:
        return True
    return False


def get_whole_datbase():
    collection = get_collection("data")
    database = collection.find({})
    return database


def delete_old_tweets(ids_to_be_deleted):
    collection = get_collection("data")
    collection.delete_many({"_id": {"$in": ids_to_be_deleted}})