from config import FIREBASE_URL
import requests
import random
import json
from tweet_entity import TweetEntity

def upload_data(tweet_information):
    random_int = random.getrandbits(128)
    data = { 
        str(random_int): {
            "id": tweet_information.tweet_id,
            "location": tweet_information.location, 
            "keywords" : tweet_information.keywords,
            "tweet_link": tweet_information.tweet_link,
            "time": tweet_information.time
        }
    }
    r = requests.patch(FIREBASE_URL, data=json.dumps(data))
    if r.status_code != 200:
        # TODO: Write into a separate error.log files
        print("Some error occurred. Error code: {}".format(r.status_code))
    
# upload_data(TweetEntity("Mumbai", "oxygen, remdesiver, ventilator, icu", "https://twitter.com/", "time"))
