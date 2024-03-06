from event_scheduler import MyEventScheduler
import argparse

def main():

    parser = argparse.ArgumentParser(description="Event Scheduler CLI")
    parser.add_argument('action', choices=['add', 'remove', 'get'], help="Action to perform")
    parser.add_argument('--title', help="Title of the event", default=None)
    parser.add_argument('--date', help="Date of the event (YYYY-MM-DD)", default=None)
    parser.add_argument('--description', help="Description of the event", default="")
    parser.add_argument('--storage', help="Path to the JSON file for storing events", default='events.json')
    args = parser.parse_args()

    scheduler = MyEventScheduler(args.storage)

    if args.action == 'add':
        if not args.title or not args.date:
            print("Adding an event requires a title and a date.")
            return
        success, message = scheduler.add_event(args.title, args.date, args.description)
        print(message)

    elif args.action == 'remove':
        if not args.title:
            print("Removing an event requires a title.")
            return
        success, message = scheduler.remove_event(args.title)
        print(message)
    
    elif args.action == 'get':
        print(scheduler.get_events())

    

if __name__ == '__main__':
    main()