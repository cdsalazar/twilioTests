from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
messages = client.messages.list(  
) 
 
# for m in messages: 
# 	if (m.direction == 'inbound'):
# 		print m.body

def returner():

	messages = client.messages.list() 
	for m in messages: 
		if (m.direction == 'inbound'):
			return m.body

print(returner())
