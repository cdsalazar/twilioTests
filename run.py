from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

 

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    message = twilio.twiml.message
    resp = twilio.twiml.Response()
    resp.message("R: " + returner())
    return str(resp)

def returner():
	messages = client.messages.list() 
	for m in messages: 
		if (m.direction == 'inbound'):
			return m.body



 
