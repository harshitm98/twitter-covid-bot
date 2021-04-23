from config import FIREBASE_URL
import requests
import random
import json
from tweet_entity import TweetEntity

# data = '''{ "yolo" : "yolo2"}'''
# r = requests.patch(FIREBASE_URL, data=data)
# print(r.content)
# print(r.status_code)

def upload_data(tweet_information):
    random_int = random.getrandbits(128)
    data = { 
        str(random_int): {
            "location": tweet_information.location, 
            "is_oxygen_available": tweet_information.is_oxygen_available,
            "is_remdesiver_available": tweet_information.is_remdesiver_available,
            "is_hospital_bed_available": tweet_information.is_hospital_bed_available,
            "is_icu_available": tweet_information.is_icu_available,
            "tweet_link": tweet_information.tweet_link,
            "time": tweet_information.time
        }
    }
    r = requests.patch(FIREBASE_URL, data=json.dumps(data))
    if r.status_code == 200:
        print("Uploaded tweet successfully")
    else:
        # TODO: Write into a separate error.log files
        print("Some error occurred. Error code: {}".format(r.status_code))
    
# upload_data(TweetEntity("Mumbai", True, True, False, True, False, "https://twitter.com/", "time"))
