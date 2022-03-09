# Introduction
My objective for this project is create a scheduler for myself, that will send text
notifications to my phone, reminding me to accomplish tasks and keep myself on tracks.

# Requirements
- Hug
- Twilio
- Python
- Pip
- HTTPIE
- sqlite_utils
- DB Browser for sqlite

run database_setup.py (make sure to change paths to your requirements)
# database_setup.py
NOTE: I use paths for the .csv files + database file based on my machine. Your mileage may vary...
# pythonsms.py
https://pypi.org/project/smsframework/
https://docs.python.org/3/library/time.html#time.sleep

This file will handle sending the text messages to my phone, using Twilio and Hug API Framework

NOTE: I created a separate file called keys where pythonsms.py will retrieve my account, key, and phone number.
It is not present in this github repository.

# tasks.py
This file will handle storing the tasks and users, as well as retreiving and sending data to tasks.py
This includes deleting items from the database.

I should come back in here and write how to use the api calls.
## Note regarding this file: the following is pseudo code for a potential solution
def searchDB():
- search the database given a username
- order the return by timestamps
- make a list with all given informatio
- for X in List:
- create a new object, whos constructor takes time, a number, and task description

The most difficult thing here might be creating the class that I can call on to create said object...

# scheduler.py
- https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
- https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/

This file will be responsible for creating the schedules and sending the signal to pythonsms.py to 
send texts. It will also call upon tasks.py to retrieve user and task data. As well as hold 
information about the TASK CLASS.

## NOTE regarding this file
- This file will not be ran using HUG. Instead, it will run indefinitely with a while loop. 
An example can be see in timetest.py. I'm hoping this will work

The following is a potential solution to creating the task object.
def searchDB():
- for X in List:
- create a new object, whos constructor takes time, a number, and task description

The most difficult thing here might be creating the class that I can call on to create said object...
- I'm thinking I might have to redo the DB again, using id, #, task, date, time.    


# Potential Work
- Change the database again, to include day and time as two seperate entities
- Figure out how to parse the incoming json form tasks.py
- Going to have to retrieve the users phone number as well. This just inludes another call to tasks.py to retrieve the phone number. There might be difficulty connecting the number with the task. Which makes me wonder if its just easier to include the phone number in the task insertion. This kind of jumbles with my current functions. I'll save that for later
- Once messages are sent out, the object needs to be deleted.