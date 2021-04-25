import requests
from config import FIREBASE_URL, FIREBASE_REPLIED_URL
import json

def get_resources_database_size():
    r = requests.get(FIREBASE_URL)
    if r.status_code != 200:
        return 0
    database = json.loads(r.text)
    return len(list(database.keys()))

def get_replies_database_size():
    r = requests.get(FIREBASE_REPLIED_URL)
    if r.status_code != 200:
        return 0
    database = json.loads(r.text)
    return len(list(database.keys()))

def get_stats():
    print("Database of tweets: {}".format(get_resources_database_size()))
    print("Number of replies sent: {}".format(get_replies_database_size()))

get_stats()