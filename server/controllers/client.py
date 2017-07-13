from flask import request
from flask_restful import Resource

from ..utils import responses

# Import the models we will interact with
from ..models.client import Client
from ..models.merchant import Merchant

class ClientController(Resource):
    def get(self, merchant_id):
        '''
        '''
        merchant_obj = Merchant.query.get(merchant_id)
        if merchant_obj == None:
            return responses.error({'error': 'No merchant for id: \'%s\'' % id})
        purchased_items = request.args
        for item in purchased_items:
            print item

