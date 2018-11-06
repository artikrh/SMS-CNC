#!/usr/bin/python
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__) # Runs in 127.0.0.1:5000 which then is advertised in the internet with ngrok
@app.route('/', methods=['POST'])

def sms():
    message_body = request.form['Body'] # Get text content from the SMS received to your Twilio SMS-capable phone number

    resp = MessagingResponse()
    resp.message(getReply(message_body))

    return str(resp)

def getReply(message):
    message = message.lower().strip()

    if "killbill2" in message:
        answer = "Killed Bill 2" # Implement arbitrary functions here such as this one which simply replies "Killed Bill 2"
    else:
        answer = "These are the commands you may use: killbill2"

    if len(answer) > 1500: # Cut answer because Twilio limits 1.6k characters in one message
        answer = answer[0:1500] + "..."

    return answer

def removeHead(fromThis, removeThis):
    if fromThis.endswith(removeThis):
        fromThis = fromThis[:-len(removeThis)].strip()
    elif fromThis.startswith(removeThis):
        fromThis = fromThis[len(removeThis):].strip()

    return fromThis

if __name__ == '__main__':
    app.run()
