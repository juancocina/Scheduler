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
#  Testing the sending function
#  ...Every time lines 21-25 are compiled, a message is sent to my phone
#  They'll be commented out to prevent spam to my phone...

message = client.messages.create(
    from_='+16066378278',
    body='this is a test',
    to=myNumber
)
print(message.sid)

#
#  Route
#
@hug.get('/')
def landing():
    return {"Status Code": "200", "Message": "PythonSMS API is up and running!"}

#
#  Sending a message function
#
@hug.post('/sendMessage')
def send(request, id: hug.types.text, phone_number: hug.types.number, task_description: hug.types.text):
    phone_number = request.params.get("phone_number")
    task_description = request.params.get("task_description")

    message = client.message.create(
        from_='+16066378278',
        body=task_description,
        to=phone_number
    )

    if(message.sid):
        #  Going to have to come back and test this line when the time comes
        #  (Its supposed to delete tasks from the DB)
        response = requests.delete(f'http://localhost:8000/deleteTask/', data={id})
        
        # send a message to tasks.py to delete the task that was just sent out
        return {"Status:": str(message.sid)}
    else:
        return {"Error": "Message Could Not be Sent"}
