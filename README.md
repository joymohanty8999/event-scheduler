1. There is no need for any external dependencies to be installed
2. The program can be run using the command: python main.py
3. You can add the events.json file to the path as the storage file where the events can be stored, removed and listed from.

4. To add an event you can use the following command as an example: python main.py add --title "COMP 646 Class" --date "2024-03-15" --storage "events.json"

5. To remove an event you can use the following command: python main.py remove --title "Meeting with Team" --storage "events.json"

6. To get all events you can use the following command: python main.py get --storage "events.json"