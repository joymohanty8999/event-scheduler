from datetime import datetime

class MyEventScheduler:

    def __init__(self):

        self.events = [] #list to add, display and remove events from

    def add_event(self, title, date, description=""):

        # Check format of data and its uniqueness
        if not self.check_valid_date(date) or self.event_title_exists(title):
            return False
        
        self.events.append({"title": title, "date": date, "description": description})

        return True

    def remove_event(self, title):

        for event in self.events:
            if event["title"] == title:
                self.events.remove(event)
                return True
            
        return False

    def get_events(self):

        if not self.events:
            print("No events scheduled.")

        for event in self.events:
            print(f"Title: {event['title']}, Date: {event['date']}, Description: {event['description']}")

    def check_valid_date(self, date):

        date_format = '%Y-%m-%d'
        parsed_date = datetime.strptime(date, date_format) # string to datetime object conversion
        formatted_date = datetime.strftime(parsed_date, date_format) # datetime object to string conversion
        return formatted_date == date # check if both return same value


    def event_title_exists(self, title):
        return any(event["title"] == title for event in self.events)

scheduler = MyEventScheduler()
scheduler.add_event("Event_1", "2024-03-10", "This is a sample event.")
scheduler.add_event("Event_2", "2024-03-15") 
scheduler.get_events()