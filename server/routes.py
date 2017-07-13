from . import api
import controllers.merchant
import controllers.client

def add_routes():
    api.add_resource(controllers.merchant.MerchantController, '/merchant/<string:id>')
    api.add_resource(controllers.client.ClientController, '/purchase/<int:client_id>/<string:merchant_id>')
