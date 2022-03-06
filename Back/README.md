# Introduction
My objective for this project is create a scheduler for myself, that will send text
notifications to my phone, reminding me to accomplish tasks and keep myself on tracks.

# Requirements
- Hug
- Twilio
- Python
- Pip
- HTTPIE

pip install sqlite-utils
run database_setup.py (make sure to change paths to your requirements)
pip install httpie

# pythonsms.py
https://pypi.org/project/smsframework/

This file will handle sending the text messages to my phone, using Twilio and Hug API Framework

NOTE: I created a separate file called keys where pythonsms.py will retrieve my account, key, and phone number.
It is not present in this github repository.

# scheduler.py

This file will handle storing the tasks and making the schedule, as well as sending the message to pythonsms.py
to be delivered to the phone number. 
## Note regarding this file: the following is pseudo code for a potential solution
def searchDB():
- search the database given a username
- order the return by timestamps
- make a list with all given informatio
- for X in List:
- create a new object, whos constructor takes time, a number, and task description

The most difficult thing here might be creating the class that I can call on to create said object...
