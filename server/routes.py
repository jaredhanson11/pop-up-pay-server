from . import api
import controllers.merchant

def add_routes():
    api.add_resource(controllers.merchant.MerchantController, '/merchant/<int:id>')
