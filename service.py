import os
from bottle import request, get, post, run
from send_sms import send_message

@get('/ping')
def ping():
    return "pong";

@post('/sms')
def send_sms():
    send_message(request.forms.get('from'), request.forms.get('to'), request.forms.get('message'))


run(host='localhost', reloader=True, port=8080)
