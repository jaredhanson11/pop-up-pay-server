from server import db
from server.models import client, merchant
db.drop_all()
db.create_all()

_merchant = merchant.Merchant.create('test-merchant', 'Lemonade Stand')
print 'Added merchant: %s' % str(_merchant.to_json())
_item = _merchant.add_menu_item('Lemonade', 1.00)
print 'Added item: %s' % str(_item.to_json())
_item = _merchant.add_menu_item('Extra Ice', .50)
print 'Added item: %s' % str(_item.to_json())

_client = client.Client.create('Test User')
print 'Added client: %s' % str({'name': _client.name, 'id': _client.id})
_client = client.Client.create('Test User 2')
print 'Added client: %s' % str({'name': _client.name, 'id': _client.id})
