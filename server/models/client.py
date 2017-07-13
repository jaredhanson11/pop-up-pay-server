from . import db

class Client(db.Model):
     __tablename__ = 'client'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(50))
    reciepts    = db.relationship('Reciept', backref='client', lazy='dynamic')