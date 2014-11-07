from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
  

app = Flask(__name__)

def parser(input):
    mod_input = input.split()
    if (mod_input[0] == "hello" and mod_input[1] == "world"):
        return "we cool"

    else:
        return "we not cool"

def returner():
    messages = client.messages.list() 
    for m in messages: 
        if (m.direction == 'inbound'):
            return parser(m.body)
            #return m.body

 
@app.route("/", methods=['GET', 'POST'])


def hello_monkey():
    resp = twilio.twiml.Response()
    resp.message("R: " + returner())
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)



