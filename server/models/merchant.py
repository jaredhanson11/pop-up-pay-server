from .. import db
from menu_item import MenuItem

class Merchant(db.Model):
    __tablename__ = 'merchant'

    id = db.Column(db.String(1000), primary_key=True)
    name = db.Column(db.String(50))
    menu = db.relationship('MenuItem', backref='merchant', lazy='dynamic')
    receipts = db.relationship('Receipt', backref='merchant', lazy='dynamic')

    def add_menu_item(self, name, price):
        return MenuItem.create(name, price, self.id)

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'menu': map(lambda menu_item: menu_item.to_json(), self.menu),
            'receipts': map(lambda receipt_item: receipt_item.to_json(), self.receipts)
        }
        return ret

    @staticmethod
    def create(id, name):
        new_merchant = Merchant(id=id, name=name)
        db.session.add(new_merchant)
        try:
            db.session.commit()
            return new_merchant
        except Exception, e:
            print e
            db.session.rollback()
            return None
