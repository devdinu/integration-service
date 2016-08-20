from instamojo_wrapper import Instamojo
import os
import pdb
import requests

class PaymentClient:

    def __init__(self):
        self.api = os.environ.get('API')
        self.auth = os.environ.get('AUTH')
        self.salt = os.environ.get('SALT')

    def create_request(self, _farmer_id, _amount, _purpose, _email, _redirect_url):
        headers = { "X-Api-Key": self.api, "X-Auth-Token": self.auth }
        payload = { 'purpose': _purpose, 'amount': _amount }
        pay_request_response = requests.post("https://test.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
        print(pay_request_response)
        return pay_request_response['longurl']

    def get_status(self, payment_req_id):
        print(response)
        return response
