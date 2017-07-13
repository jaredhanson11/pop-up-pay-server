from flask_restful import Resource

from ..utils import responses

# Import the models we will interact with
from ..models.merchant import Merchant

class MerchantController(Resource):
    def get(self, id):
        '''
        Returns all the current records.
        '''
        merchant_obj = Merchant.query.get(id)
        if merchant_obj:
            merchant_json = merchant_obj.to_json()
            return responses.success({'merchant': merchant_json})
        else:
            return responses.error({'error': 'No merchant for id: \'%s\'' % id})

