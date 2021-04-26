from config import FIREBASE_URL, FIREBASE_REPLIED_URL, emailid, password, WEB_API_KEY
import requests
import random
import json
from tweet_entity import TweetEntity


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

def upload_data(data_to_upload):
    auth_token = authenticate_firebase()
    r = requests.patch(FIREBASE_URL, data=json.dumps(data_to_upload), params = auth_token)
    if r.status_code != 200:
        # TODO: Write into a separate error.log files
        print("Some error occurred. Error code: {}".format(r.status_code))
        
def upload_replied(tweet_id):
    random_int = random.getrandbits(128)
    data = { str(random_int) : str(tweet_id) }
    auth_token = authenticate_firebase()
    r = requests.patch(FIREBASE_REPLIED_URL, data=json.dumps(data), params = auth_token)
    if r.status_code != 200:
        print("Some error occured. Error code: {}".format(r.status_code))
    else:
        print("Replied with resources!")
    
#  upload_data(TweetEntity("12323456789" , "Mumbai", "oxygen, remdesiver, ventilator, icu", "https://twitter.com/", "time"))
