from flask import request
from flask_restful import Resource

from ..utils import responses

# Import the models we will interact with
from ..models.client import Client
from ..models.merchant import Merchant
from ..models.receipt import Receipt

class ClientController(Resource):
    def get(self, client_id, merchant_id):
        '''
        Handles purchasing and setting receipts
        '''

        purchased = []
        error = []

        client_obj = Client.query.get(client_id)
        if client_obj == None:
            return responses.error({'error': 'No user for id: \'%s\'' % id})

        merchant_obj = Merchant.query.get(merchant_id)
        if merchant_obj == None:
            return responses.error({'error': 'No merchant for id: \'%s\'' % id})

        new_receipt = Receipt.empty_receipt(client_id, merchant_id)

        purchased_items = request.args
        for item in purchased_items:
            _item = merchant_obj.menu.filter_by(id=item).first()
            if _item == None:
                error.append({'id: ' + str(item): purchased_items.get(item)})
            else:
                _item_id = _item.id
                quantity = purchased_items.get(item)
                new_receipt.add_item(_item_id, quantity)
                purchased.append({_item.name: purchased_items.get(item)})
        return responses.success({'purchased': purchased, 'error': error})

