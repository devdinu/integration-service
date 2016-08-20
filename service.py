import os
from bottle import request, get, post, run, response
from twilio_client import *
from twilio import twiml
from payment import PaymentClient

client = TwilioClient()
paymentClient = PaymentClient()

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            return fn(*args, **kwargs)

    return _enable_cors


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

@enable_cors
@post('/payments/<farmer_id>/create')
def create_payment_request(farmer_id):
    return paymentClient.create_request(farmer_id, request.forms.get('amount'), request.forms.get('purpose'))

run(host='localhost', reloader=True, port=8080)
