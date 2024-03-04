import json
from datetime import datetime

class MyEventScheduler:

    def __init__(self, events_file = 'events.json'):

        self.events = [] #list to add, display and remove events from
        self.events_file = events_file
        self.load_events()

    def add_event(self, title, date, description=""):

        # Check format of data and its uniqueness
        if not self.check_valid_date(date) or self.event_title_exists(title):
            return False, "Invalid date format, or event already exists"
        
        self.events.append({"title": title, "date": date, "description": description})
        self.save_events()

        return True, "Addition of event is successful"

    def remove_event(self, title):

        for event in self.events:
            if event["title"] == title:
                self.events.remove(event)
                self.save_events()
                return True, "Deletion of event is successful"
            
        return False

    def get_events(self):

        if not self.events:
            print("No events scheduled.")

        for event in self.events:
            print(f"Title: {event['title']}, Date: {event['date']}, Description: {event['description']}")

    def save_events(self):

        with open(self.events_file, 'w') as file:
            json.dump(self.events, file)


    def load_events(self):

        try:
            with open(self.events_file, 'r') as file:
                self.events = json.load(file)

        except FileNotFoundError:
            self.events = []

    def check_valid_date(self, date):

        date_format = '%Y-%m-%d'
        parsed_date = datetime.strptime(date, date_format) # string to datetime object conversion
        formatted_date = datetime.strftime(parsed_date, date_format) # datetime object to string conversion
        return formatted_date == date # check if both return same value


    def event_title_exists(self, title):
        return any(event["title"] == title for event in self.events)

scheduler = MyEventScheduler()
scheduler.add_event("COMP 539 Presentation", "2024-03-10", "Present your Pitch to the class")
scheduler.add_event("COMP 646 Class", "2024-03-15") 
scheduler.get_events()