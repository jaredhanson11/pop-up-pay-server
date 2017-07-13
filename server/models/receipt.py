from datetime import datetime
from .. import db

from receipt_item import ReceiptItem

class Receipt(db.Model):
    __tablename__ = 'receipt'

    id = db.Column(db.Integer, primary_key=True)
    purchased_at = db.Column(db.DateTime, server_default=db.func.now())
    merchant_id = db.Column(db.String(1000), db.ForeignKey('merchant.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    items = db.relationship('ReceiptItem', backref='receipt', lazy='dynamic')

    def add_item(self, menu_item_id, quantity):
        return ReceiptItem.create(menu_item_id, self.id, quantity)

    def to_json(self):
        ret = {
            'id': self.id,
            'purchased_at': self.purchased_at.strftime('%c'),
            'merchant_id': self.merchant_id,
            'client_id': self.client_id,
            'items': map(lambda menu_item: menu_item.to_json(), self.items)
        }
        return ret

    @staticmethod
    def empty_receipt(client_id, merchant_id):
        new_receipt = Receipt(purchased_at=datetime.now(), client_id=client_id, merchant_id=merchant_id)
        db.session.add(new_receipt)
        try:
            db.session.commit()
            return new_receipt
        except Exception, e:
            print e
            db.session.rollback()
            return None

