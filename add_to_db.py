from config import FIREBASE_URL, FIREBASE_REPLIED_URL, emailid, password, WEB_API_KEY, WEB_API_KEY_NEW, FIREBASE_NEW_REPLIED_URL, FIREBASE_NEW_URL
import requests
import random
import json
from tweet_entity import TweetEntity
from auth import get_collection


def authenticate_firebase():
    headers = {'Content-Type': 'application/json',}
    params = (('key', WEB_API_KEY),)
    val = {
        "email" : emailid,
        "password": password,
        "returnSecureToken": "true"
    }
    data = str(val)
    auth_token = (('auth', ''),)
    try:
        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword', headers=headers, params=params, data=data)
        output = response.json()
        key = output['localId']
        token = output['idToken']
        auth_token = (('auth', token),)
    except:
        print("Authentication error!")
    return auth_token

def upload_replied(tweet_id):
    random_int = random.getrandbits(128)
    data = { str(random_int) : str(tweet_id) }
    auth_token = authenticate_firebase()
    r = requests.patch(FIREBASE_REPLIED_URL, data=json.dumps(data), params = auth_token)
    if r.status_code != 200:
        print("Some error occured. Error code: {}".format(r.status_code))
    else:
        print("Replied with resources!")
        
def authenticate_fetcher_database():
    headers = {'Content-Type': 'application/json',}
    params = (('key',   WEB_API_KEY_NEW),)
    val = {
        "email" : emailid,
        "password": password,
        "returnSecureToken": "true"
    }
    data = str(val)
    auth_token = (('auth', ''),)
    try:
        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword', headers=headers, params=params, data=data)
        output = response.json()
        key = output['localId']
        token = output['idToken']
        auth_token = (('auth', token),)
    except:
        print("Authentication error!")
    return auth_token

def upload_data(list_of_data):
    collection = get_collection("data")
    collection.insert_many(list_of_data)

def is_exists_in_database(tweet_id):
    collection = get_collection("data")
    if collection.find_one({"tweet_id": str(tweet_id)}) != None:
        return True
    return False

