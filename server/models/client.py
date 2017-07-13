from .. import db

class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    receipts = db.relationship('Receipt', backref='client', lazy='dynamic')

    def to_json(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'receipts': map(lambda receipt: receipt.to_json(), self.receipts)
        }
        return ret

    @staticmethod
    def create(name):
        new_client = Client(name=name)
        db.session.add(new_client)
        try:
            db.session.commit()
            return new_client
        except Exception, e:
            print e
            db.session.rollback()
            return None
