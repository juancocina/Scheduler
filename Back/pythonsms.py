'''
    Juan Cocina, 1/19/2022
    The purpose of this file to is to send text messages to a given phone number (likely my own)
'''

#  imports
from urllib import response
from twilio.rest import Client
import hug
import requests
import json
from datetime import datetime
import keys

#  Account Sid and Auth Token from twilio.com
account_sid = keys.accountSid()
auth_token = keys.authToken()
myNumber = keys.phone()  # this will have be adjusted to take different phone numbers depending on the user

client = Client(account_sid, auth_token)

#
#  Sending a message function
#
@hug.post('/sendMessage')
def send(body):
    task_description = body['task_description']
    phone_number = body['phone_number']
    id = body['id']

    message = client.messages.create(
        from_= myNumber,
        body=task_description,
        to=phone_number
    )

    if(message.sid):
        #  Going to have to come back and test this line when the time comes
        #  (Its supposed to delete tasks from the DB)
        response = requests.delete(f'http://localhost:8000/deleteTask/{id}')
        
        # send a message to tasks.py to delete the task that was just sent out
        return response.json()
    else:
        return response.json()