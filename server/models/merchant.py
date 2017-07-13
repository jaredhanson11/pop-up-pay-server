from . import db

class Merchant(db.Model):
     __tablename__ = 'merchant'

    id = db.Column(db.String(1000), primary_key=True)
    name = db.Column(db.String(50))
    menu = db.relationship('MenuItem', backref='merchant', lazy='dynamic')
    reciepts = db.relationship('Reciept', backref='merchant', lazy='dynamic')

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'menu': map(self.menu, lambda menu_item: menu_item.to_json())
            'receipts': map(self.reciepts, lambda reciepts_item: reciepts.to_json())

        }
        return ret