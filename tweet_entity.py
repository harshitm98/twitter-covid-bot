class TweetEntity:
    location = "None"
    keywords = []
    tweet_link = False
    time = False
    
    def __init__(self, location, keywords, tweet_link, time):
        self.location = location
        self.keywords = keywords
        self.tweet_link = tweet_link
        self.time = time
        
    
    def set_location(self, _location):
        self.location = _location
        
    def set_keywords(self, _keywords):
        self.keywords = _keywords
        
    def set_time(self, _time):
        self.time = _time
    