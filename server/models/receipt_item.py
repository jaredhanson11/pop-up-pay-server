from .. import db

class ReceiptItem(db.Model):
    __tablename__ = 'receipt_item'
    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'))
    quantity = db.Column(db.Integer)

