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

pip install sqlite-utils
run database_setup.py (make sure to change paths to your requirements)
pip install httpie

# database_setup.py
NOTE: I use paths for the .csv files + database file based on my machine. Your mileage may vary...
# pythonsms.py
https://pypi.org/project/smsframework/

This file will handle sending the text messages to my phone, using Twilio and Hug API Framework

NOTE: I created a separate file called keys where pythonsms.py will retrieve my account, key, and phone number.
It is not present in this github repository.

# tasks.py

This file will handle storing the tasks and users, as well as retreiving and sending data to tasks.py
## Note regarding this file: the following is pseudo code for a potential solution
def searchDB():
- search the database given a username
- order the return by timestamps
- make a list with all given informatio
- for X in List:
- create a new object, whos constructor takes time, a number, and task description

The most difficult thing here might be creating the class that I can call on to create said object...


CURRENT STATUS: NEED TO FIX THE DELETE FUNCTION

# scheduler.py
This file will be responsible for creating the schedules and sending the signal to pythonsms.py to 
send texts. It will also call upon tasks.py to retrieve user and task data. As well as hold 
information about the TASK CLASS.

## NOTE regarding this file
- This file will not be ran using HUG. Instead, it will run indefinitely with a while loop. 
An example can be see in timetest.py. I'm hoping this will work

The following is a potential solution to creating the task object.
def searchDB():
- search the database given a username
- order the return by timestamps
- make a list with all given informatio
- for X in List:
- create a new object, whos constructor takes time, a number, and task description

The most difficult thing here might be creating the class that I can call on to create said object...


# Potential Work
I can break down the current Database structure even further, making it more simple to store tasks.
In scheduler, I should create a class dedicated to creating new 'schedule' jobs.
It doesn't make sense to me to do that in Tasks.py