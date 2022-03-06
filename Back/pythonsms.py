'''
    Juan Cocina, 1/19/2022
    The purpose of this file to is to send text messages to a given phone number (likely my own)
'''

#  imports
from twilio.rest import Client
import hug
import requests
import json
from datetime import datetime
import keys

#  Account Sid and Auth Token from twilio.com
account_sid = 'AC3c6db669ecfa6a4b4c8a9b517be63439'
auth_token = '7d41a9e19c482c527200b67ca4516ece'

client = Client(account_sid, auth_token)


#
#  Testing the sending function
#  ...Every time lines 21-25 are compiled, a message is sent to my phone
#  They'll be commented out to prevent spam to my phone...
'''
message = client.messages.create(
    from_='+16066378278',
    body='this is a test',
    to='+13235097821'
)
'''

#
#  Route
#
@hug.get('/')
def landing():
    return {"Status Code": "200", "Message": "PythonSMS API is up and running!"}

#
#  Sending a message function
#
