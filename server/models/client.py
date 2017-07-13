from .. import db

class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    receipts = db.relationship('Receipt', backref='client', lazy='dynamic')

    @staticmethod
    def create(id, name):
        new_client = Client(id, name)
        db.session.add(new_client)
        try:
            db.session.commit()
            return new_client
        except Exception, e:
            print e
            db.session.rollback()
            return None
