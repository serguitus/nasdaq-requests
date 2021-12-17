import enum
from datetime import date

from app import db


class OperationTypeEnum(enum.Enum):
    sell = 'sell'
    buy = 'buy'


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

    def total_held(self):
        return self.shares * self.value


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(4), index=True)
    shares = db.Column(db.Integer)
    value = db.Column(db.Float)
    date = db.Column(db.DateTime)
    type = db.Column(
        db.Enum(OperationTypeEnum),
        default=OperationTypeEnum.buy,
        nullable=False
    )

    def __repr__(self):
        return '<Operation %r - %r>' % (self.symbol, self.type)

    def update_or_create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def total_bought(cls, symbol):
        """ gives total value bouth for specified Stock """
        total = 0
        ops = Operation.query.filter_by(
            symbol=symbol, type=OperationTypeEnum.buy).all()
        for op in ops:
            total += (op.shares * op.value)
        return total

    @classmethod
    def total_sold(cls, symbol):
        """ gives total value sold for specified Stock """
        total = 0
        ops = Operation.query.filter_by(
            symbol=symbol, type=OperationTypeEnum.sell).all()
        for op in ops:
            total += (op.shares * op.value)
        return total

    @classmethod
    def get_max_today(cls, symbol):
        ops = cls.query.filter(cls.symbol == symbol, cls.date >= date.today())
        max = 0
        for op in ops:
            if op.value > max:
                max = op.value
        return max

    @classmethod
    def get_min_today(cls, symbol):
        ops = cls.query.filter(cls.symbol == symbol, cls.date >= date.today())
        if not ops.count():
            return 0
        min = ops.first().value
        for op in ops:
            if op.value < min:
                min = op.value
        return min

    @classmethod
    def get_ave_today(cls, symbol):
        ops = cls.query.filter(cls.symbol == symbol, cls.date >= date.today())
        if not ops.count():
            return 0
        ave = 0
        for op in ops:
            ave += op.value
        return ave / ops.count()
