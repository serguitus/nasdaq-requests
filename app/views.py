import json
import time
import requests
from flask_expects_json import expects_json
from flask import request, jsonify

from . import app, db
from app.models import Stock
from app.schema import stocks_schema, stock_schema

# valid trade payload schema
trade_schema = {
    "type": "object",
    "properties": {
        "amount": {"type": "number"},
        "buy": {"type": "boolean"}
    },
    "required": ['amount', 'buy']
}


@app.route('/trade/<symbol>', methods=['GET', 'POST'])
@expects_json(trade_schema)
def trade(symbol):
    # check symbol exists
    nasdaq_url = 'https://api.nasdaq.com/api/quote/{}/info?assetclass=stocks'
    # fake user agent to bypass nasdaq protection
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    stock_data = requests.get(nasdaq_url.format(symbol), headers=headers)
    json_response = json.loads(stock_data.text)
    if json_response['status']['rCode'] != 200:
        return {'error': "That Symbol is invalid"}

    amount = request.json['amount']

    # update or create?
    db_stock = Stock.query.filter_by(symbol=symbol).first()
    if db_stock:
        if not request.json['buy']:
            # when selling, amount is substracted
            amount = -1 * request.json['amount']
        # already bougth some shares there. add more
        db_stock.shares += amount
        db_stock.update_or_create()
        return stock_schema.dump(db_stock)
    else:
        # new stock. create it!
        new_stock = Stock(symbol=symbol, shares=amount, value=float(
            json_response['data']['primaryData']['lastSalePrice'][1:]))
        new_stock.update_or_create()
        return new_stock


@app.route('/stocks/')
def get_stocks():
    stocks = Stock.query.all()
    return {'stocks': stocks_schema.dump(stocks)}
