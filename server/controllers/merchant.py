from flask_restful import Resource

from ..utils import responses

# Import the models we will interact with
from ..models.merchant import Merchant

class MerchantController(Resource):
    def get(self, id):
        '''
        Returns all the current records.
        '''
        merchant = Merchant.get(id)
        merchant_json = merchant.to_json()
        return responses.success({'merchant': merchant_json})

