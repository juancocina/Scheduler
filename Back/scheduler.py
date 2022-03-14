'''
    Juan Cocina 3/6/2022
    This file is dedicated to calling tasks.py for user/task information, and sending
    signals to pythonsms.py to send texts
'''
import schedule
import time
import datetime
from datetime import datetime
# import json
import requests

#
#   Job dedicated to scanning tasks in the DB & checking if they should be send
#
def scanDB():
    retrieved_tasks = requests.get(f'http://localhost:8000/retrieveAllTasks/')
    now = datetime.now()
    current_time = now.strftime("%I:%M%p") 
    current_date = now.strftime("%Y-%m-%d")

    tasks = retrieved_tasks.json()
    
    if retrieved_tasks.status_code == 200:
        for x in tasks:  #  access the tasks
            for y in tasks[x]:  #  iterate through the tasks + we can access specific variables now
                if y['time'] == current_time and y['date'] == current_date:
                    # print(y) uncomment this line to see the task print in terminal

                    #  send text
                    payload = {
                        'id': y['id'],
                        'phone_number': y['phone_number'],
                        'task_description': y['task_description']
                    }
                    response = requests.post('http://localhost:8001/sendMessage/', data=payload)
    else:
        print({"Status Code": "500", "Message": "Could not retreive from the DB..."})

#   List of current Jobs
schedule.every().minute.at(":00").do(scanDB)

#   Loop to keep the script running and scheduled jobs going
while True:
    schedule.run_pending()
    time.sleep(1)

