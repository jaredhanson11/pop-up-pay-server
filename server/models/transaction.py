from .. import db

class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.String(1000), primary_key=True)

    def to_json(self):
        ret = {
            'id': self.id,
            'completed': True
        }
        return ret

    @staticmethod
    def create(transaction_id):
        new_item = Transaction(id=transaction_id)
        db.session.add(new_item)
        try:
            db.session.commit()
            return new_item
        except Exception, e:
            print e
            db.session.rollback()
            return None
