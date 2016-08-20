import os
from bottle import request, get, post, run
from twilio_client import *
from twilio import twiml


client = TwilioClient()

@get('/ping')
def ping():
    return "pong";

@post('/sms')
def send_sms():
    client.send_message(request.forms.get('from'), request.forms.get('to'), request.forms.get('message'))

@post('/notify_farmer')
def notify_farmer():
    client.make_call(request.forms.get('to_number'))

def get_response_for_farmer():
    response = twiml.Response().say("Welcome to Fund Farmers", voice='alice')
    return response

run(host='localhost', reloader=True, port=8080)
