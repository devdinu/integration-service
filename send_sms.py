import sys
import os


from twilio.rest import TwilioRestClient

def send_message(from_user, to_user, body_content):
    client = TwilioRestClient(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))
    client.messages.create(to=to_user, from_=from_user, body=body_content)
