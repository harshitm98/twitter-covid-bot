class TweetEntity:
    tweet_id = ""
    location = "None"
    keywords = []
    tweet_link = False
    time = False
    tweet_text = ""
    
    def __init__(self, tweet_id, location, keywords, tweet_link, time, tweet_text):
        self.tweet_id = tweet_id
        self.location = location
        self.keywords = keywords
        self.tweet_link = tweet_link
        self.time = time
        self.tweet_text = tweet_text
        
    def set_tweet_id(self, tweet_id):
        self.tweet_id = tweet_id
    
    def set_location(self, _location):
        self.location = _location
        
    def set_keywords(self, _keywords):
        self.keywords = _keywords
        
    def set_time(self, _time):
        self.time = _time
    