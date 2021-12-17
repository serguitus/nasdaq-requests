import enum

from app import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(4), index=True)
    shares = db.Column(db.Integer)
    value = db.Column(db.Float)
    profit_percent = db.Column(db.Float)
    # reference prices
    price_min = db.Column(db.Float)
    price_max = db.Column(db.Float)
    price_ave = db.Column(db.Float)

    def __repr__(self):
        return '<Stock %r>' % self.symbol

    def update_or_create(self):
        db.session.add(self)
        db.session.commit()
