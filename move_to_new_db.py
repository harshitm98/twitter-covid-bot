import json
from pymongo import MongoClient
from config import FIREBASE_NEW_URL, FIREBASE_NEW_REPLIED_URL, MONGO_USERNAME, MONGO_PASSWORD
import requests

def upload_tweet_data():
      r = requests.get(FIREBASE_NEW_URL)
      database = json.loads(r.text)
      connection_url = "mongodb+srv://{}:{}@cluster0.h2ugs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(MONGO_USERNAME, MONGO_PASSWORD)
      cluster = MongoClient(connection_url)
      db = cluster["tweet"]
      collection = db["data"]

      list_of_data = []
      for key in database.keys():
            data = {}
            data["_id"] = key
            data["tweet_id"] = str(database[key]["id"])
            data["location"] = database[key]["location"]
            data["keywords"] = database[key]["keywords"]
            data["time"] = database[key]["time"]
            data["tweet_link"] = database[key]["tweet_link"]
            try:
                  data["tweet_text"] = database[key]["tweet_text"]
            except:
                  data["tweet_text"] = "Please click the source to read this tweet"
            list_of_data.append(data)

      collection.insert_many(list_of_data)
      
def upload_reply_data():
      r = requests.get(FIREBASE_NEW_REPLIED_URL)
      database = json.loads(r.text)
      connection_url = "mongodb+srv://{}:{}@cluster0.h2ugs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(MONGO_USERNAME, MONGO_PASSWORD)
      cluster = MongoClient(connection_url)
      db = cluster["tweet"]
      collection = db["reply"]
      
      list_of_data = []
      for key in database.keys():
            data = {}
            data["_id"] = key
            data["tweet_id"] = database[key]
            
            data["location"] = database[key]["location"]
            data["keywords"] = database[key]["keywords"]
            data["time"] = database[key]["time"]
            data["tweet_link"] = database[key]["tweet_link"]
            try:
                  data["tweet_text"] = database[key]["tweet_text"]
            except:
                  data["tweet_text"] = "Please click the source to read this tweet"
            list_of_data.append(data)

      collection.insert_many(list_of_data)


upload_tweet_data()