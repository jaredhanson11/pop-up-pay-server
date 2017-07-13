from . import db

class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(50))
    price   = db.Column(db.Float)
    merchant_id = db.Column(db.String(1000), db.ForeignKey('merchant.id'))