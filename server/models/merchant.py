from . import db

class Merchant(db.Model):
     __tablename__ = 'merchant'

    id          = db.Column(db.String(1000))
    name        = db.Column(db.String(50))
    menu        = db.relationship('MenuItem', backref='merchant', lazy='dynamic')
    reciepts    = db.relationship('Reciept', backref='merchant', lazy='dynamic')