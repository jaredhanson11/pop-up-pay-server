from flask import request
from flask_restful import Resource

from ..utils import responses

from ..models.transaction import Transaction

class TransactionController(Resource):
    def get(self, transaction_id):
        transaction_completed = Transaction.query.get(transaction_id)
        if transaction_completed == None:
            return responses.error({'error': 'No transaction for id: %s' % transaction_id})
        return responses.success({'transaction': transaction_id})
