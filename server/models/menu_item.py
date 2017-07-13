from .. import db

class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    merchant_id = db.Column(db.String(1000), db.ForeignKey('merchant.id'))

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'merchant_id': self.merchant_id
        }
        return ret

    @staticmethod
    def create(name, price, merchant_id):
        new_item = MenuItem(name=name, price=price, merchant_id=merchant_id)
        db.session.add(new_item)
        try:
            db.session.commit()
            return new_item
        except Exception, e:
            print e
            db.session.rollback()
            return None
