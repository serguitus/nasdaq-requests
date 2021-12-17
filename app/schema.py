from app import ma
from app.models import Stock


class StockSchema(ma.Schema):
    class Meta:
        fields = ("id", "symbol", "shares", "value",
                  "profit_percent", "price_min", "price_max", "price_ave")
        model = Stock


stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)
