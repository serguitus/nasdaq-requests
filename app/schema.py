from app import ma
from app.models import Stock, Operation


class StockSchema(ma.Schema):
    class Meta:
        fields = ("id", "symbol", "shares", "value",
                  "profit_percent", "price_min", "price_max", "price_ave")
        model = Stock


stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)


class OperationSchema(ma.Schema):
    class Meta:
        fields = ("id", "symbol", "shares", "value",
                  "date")
        model = Operation


operation_schema = OperationSchema()
operations_schema = OperationSchema(many=True)
