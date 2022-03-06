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

# scheduler.py

This file will handle storing the tasks and making the schedule, as well as sending the message to pythonsms.py
to be delivered to the phone number. 


