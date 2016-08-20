from instamojo_wrapper import Instamojo
import os
import pdb
import requests
import json

class PaymentClient:

    def __init__(self):
        self.api = os.environ.get('API')
        self.auth = os.environ.get('AUTH')
        self.salt = os.environ.get('SALT')

    def create_request(self, _farmer_id, _amount, _purpose):
        headers = { "X-Api-Key": self.api, "X-Auth-Token": self.auth }
        payload = { 'purpose': _purpose, 'amount': _amount, 'buyer_email': "abc@gmail.com", 'redirect_url': "http://localhost:3000/"}
        pay_request_response = requests.post("https://test.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
        print(pay_request_response)
        return pay_request_response.json()

    def get_status(self, payment_req_id):
        print(response)
        return response
