import sys
import os
import pdb

from twilio.rest import TwilioRestClient

class TwilioClient:

    def __init__(self):
        self.client = TwilioRestClient(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))

    def send_message(self, from_user, to_user, body_content):
        self.client.messages.create(to=to_user, from_=from_user, body=body_content)

    def make_call(self, to_number):
        from_number = os.environ.get('TWILIO_CALLER_ID')
        print("to", to_number)
        call = self.client.calls.create(url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient', to=to_number, from_=from_number)
        print("this is completed!", call.sid)
