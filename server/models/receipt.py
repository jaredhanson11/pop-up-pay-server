from . import db

class Receipt(db.Model):
    __tablename__ = 'receipt'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, server_default=db.func.now())
    merchant_id = db.Column(db.String(1000), db.ForeignKey('merchant.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    items = db.relationship('MenuItem', backref='reciept', lazy='dynamic')