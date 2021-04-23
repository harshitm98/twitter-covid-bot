class TweetEntity:
    location = "None"
    is_oxygen_available = False
    is_remdesiver_available = False
    is_ventilator_available = False
    is_hospital_bed_available = False
    is_icu_available = False
    tweet_link = False
    time = False
    
    def __init__(self, location, is_oxygen_available, is_remdesiver_available, is_ventilator_available, is_hospital_bed_available, is_icu_available, tweet_link, time):
        self.location = location
        self.is_oxygen_available = is_oxygen_available
        self.is_remdesiver_available = is_remdesiver_available
        self.is_ventilator_available = is_ventilator_available
        self.is_hospital_bed_available = is_hospital_bed_available
        self.is_icu_available = is_icu_available
        self.tweet_link = tweet_link
        self.time = time
        
    
    def set_location(self, _location):
        self.location = _location
        
    def set_oxygen_available(self, _is_oxygen_available):
        self.is_oxygen_available = _is_oxygen_available
        
    def set_remdesiver_available(self, _is_remdesiver_available):
        self.is_remdesiver_available = _is_remdesiver_available
        
    def set_ventilator_available(self, _is_ventilator_available):
        self.is_ventilator_available = _is_ventilator_available
        
    def set_hospital_bed_available(self, _is_hospital_bed_available):
        self.is_hospital_bed_available = _is_hospital_bed_available
        
    def set_icu_available(self, _is_icu_available):
        self.is_icu_available = _is_icu_available
        
    def set_time(self, _time):
        self.time = _time
    