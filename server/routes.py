from . import api
import controllers.merchant
import controllers.client
import controllers.transaction

def add_routes():
    api.add_resource(controllers.merchant.MerchantController, '/merchant/<string:id>')
    api.add_resource(controllers.client.ClientBuyController, '/purchase/<int:client_id>/<string:merchant_id>/<string:transaction_id>')
    api.add_resource(controllers.transaction.TransactionController, '/transactions/<string:transaction_id>')
