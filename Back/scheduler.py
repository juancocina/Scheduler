'''
    Juan Cocina 3/6/2022
    This file is dedicated to calling tasks.py for user/task information, and sending
    signals to pythonsms.py to send texts
'''
import schedule
import time
import datetime
from datetime import datetime
import json
import requests
import hug

# Global Variables 
list_of_tasks = []

#
#   Class Task dedicated to creating objects called tasks
#
class Task:
    def __init__(self, task_id, phone_number, task_description, date, time):
        self.id = task_id
        self.number = phone_number
        self.task_desc = task_description
        self.date = date
        self.time = time

        # parse the date into an English day of the week
        y, m, d = (int(x) for x in date.split('-'))  
        day = datetime.date(y, m, d)
        self.day = day.strftime("%A")
        
        # Assign schedule based on the result
        '''
        if self.day == 'Monday':
            self.schedule = schedule.every().monday.at(self.time).do(sendOut(self))
        elif self.day == 'Tuesday':
            self.schedule = schedule.every().tuesday.at(self.time).do(sendOut(self))
        elif self.day == 'Wednesday':
            self.schedule = schedule.every().wednesday.at(self.time).do(sendOut(self))
        elif self.day == 'Thursday':
            self.schedule = schedule.every().thursday.at(self.time).do(sendOut(self))
        elif self.day == 'Friday':
            self.schedule = schedule.every().friday.at(self.time).do(sendOut(self))
        elif self.day == 'Saturday':
            self.schedule = schedule.every().saturday.at(self.time).do(sendOut(self))
        elif self.day == 'Sunday':
            self.schedule = schedule.every().sunday.at(self.time).do(sendOut(self))
        '''
#
#   End of Task class
#

#
#   Job dedicated to scanning/retrieving tasks from the BD
#
def scanDB():
    retrieved_tasks = requests.get(f'http://localhost:8000/retrieveAllTasks/')
    result = retrieved_tasks.json()
    print(result)
    tasks = []  #  list tasks from results

    # parse from JSON and create Task objects for x in results
    for x in result:
        print('test')

#
#   Function dedicated to sending the signal to pythonsms.py, to send the text
#
def sendOut():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    for x in list_of_tasks:
        if x.time == current_time:
            payload = {
                'id': x.id,
                'phone_number': x.phone_number,
                'task_description': x.task_description,
            }
            requests.post(f'http://localhost:8001/sendMessage/', data=payload)
            list_of_tasks.remove(x)


#
#   Testing class
#
def test1():
    #t1 = Task(2, '+13235097821', 'this is a test', '2022-3-8', '16:38')
    #print(t1.id)
    #print(t1.day)
    #print(t1.time)
    #print(t1.schedule)
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S") 
    print(current_time)

#   List of current Jobs
schedule.every(10).seconds.do(test1)
# check to see if texts need to be sent every minute...
# schedule.every(60).seconds.do(sendOut)

#   Loop to keep the script running and scheduled jobs going
while True:
    schedule.run_pending()
    time.sleep(1)

