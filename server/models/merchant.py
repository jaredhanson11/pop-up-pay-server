from . import db

class Mercant(db.Model):
    id          = db.Column(db.String(1000))
    name        = db.Column(db.String(50))
    menu        = db.relationship('Menu', backref='merchant', lazy='dynamic')
    reciepts    = db.relationship('Menu', backref='merchant', lazy='dynamic')