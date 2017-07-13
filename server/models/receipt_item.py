from .. import db

from menu_item import MenuItem

class ReceiptItem(db.Model):
    __tablename__ = 'receipt_item'

    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'))
    quantity = db.Column(db.Integer)

    def to_json(self):
        ret = {
            'id': self.id,
            'menu_item': MenuItem.query.get(self.menu_item_id).to_json(),
            'receipt_id': self.receipt_id,
            'quantity': self.quantity
        }
        return ret

    @staticmethod
    def create(menu_item_id, receipt_id, quantity):
        new_item = ReceiptItem(menu_item_id=menu_item_id, receipt_id=receipt_id, quantity=quantity)
        db.session.add(new_item)
        try:
            db.session.commit()
            return new_item
        except Exception, e:
            print e
            db.session.rollback()
            return None
