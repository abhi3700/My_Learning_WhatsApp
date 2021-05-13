"""
    Demo
    ====
    user: 
        hello
    bot: 
        You said: hello
"""
# from flask import Flask
# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)

# # the request will be coming to this helloworld endpoint
# @app.route("/helloworld", methods=['POST'])
# def helloworld():
# 	# E.g. if the user-> hello, then bot-> hello
# 	incoming_msg = request.values.get('Body', '').lower()		# try to get the value with key 'Body', or else return empty as ''
	
# 	# this format is suggested by Twilio
# 	response =  MessagingResponse()
# 	message = response.message()
# 	response.append(message)
# 	return str(response)

# if __name__ == '__main__':
# 	app.run(debug=True)		# to run the server. By default, the app runs on port no. 5000




import os
from twilio.rest import Client

account_sid = 'ACf2fb92754c70a4b92beec1fb453f14a2'
auth_token = '32ddd054275344e52f094f6d8c55a535'

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+8146210685'
                          )

print(message.sid)