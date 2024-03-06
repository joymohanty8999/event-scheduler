from event_scheduler import MyEventScheduler
import argparse

def main():

    event_scheduler = MyEventScheduler('events.json')

    title = "COMP 539 Presentation"
    date = "2024-03-10"
    description = "Present your Pitch to the class."
    success, message = event_scheduler.add_event(title, date, description)
    print(message)

    title = "COMP 646 Class"
    date = "2024-03-15"
    success, message = event_scheduler.add_event(title, date)
    print(message)
    
    # Listing all events
    print("\nCurrent Events:")
    print(event_scheduler.get_events())
    
    # Removing an event
    title = "COMP 646 Class"
    success, message = event_scheduler.remove_event(title)
    print("\nAfter Removal:")
    print(message)
    print(event_scheduler.get_events())

    

if __name__ == '__main__':
    main()