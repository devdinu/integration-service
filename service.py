import os
from bottle import request, get, post, run
from twilio_client import *
from twilio import twiml
from payment import PaymentClient

client = TwilioClient()
paymentClient = PaymentClient()

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

@post('/payments/<farmer_id>/create')
def create_payment_request(farmer_id):
    return paymentClient.create_request(farmer_id, request.forms.get('amount'), request.forms.get('purpose'), request.forms.get('buyer_email'), request.forms.get('redirect_url'))

run(host='localhost', reloader=True, port=8080)
