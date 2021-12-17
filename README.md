# nasdaq-requests
a simple API to do basic actions with nasdaq

for installing

Once cloned, while being at the root of the folder, first define virtual environment
`python3 -m venev env`

then activate environment
`. ./env/bin/activate`

install requirements
`pip install -r requirements.txt`

create database
`flask db upgrade`

and run app...
`flask run`

If everything goes fine, you should be able to test the endpoints
## Buy or sell shares of some stock
a POST request to `/trade/<symbol>` will create or update a held stock with the specified amount

Example request payload to `/trade/AAPL`
```
{
    "amount": 2,
    "buy": false
}
```
will add 2 shares to held stock of AAPL or create it with that amount
for selling, just set `buy` property to `false`
## Get stocks
a GET request to /stocks with give you the list of holded stocks

Example Response
```
{
    "stocks": [
        {
            "id": 1,
            "price_ave": 172.25,
            "price_max": 173.04,
            "price_min": 172.46,
            "profit_percent": null,
            "shares": 5,
            "symbol": "AAPL",
            "value": 172.26
        }
    ]
}
```
## Get History
a GET request to /history/<symbol> will give you historical data

Example Response
```
{
    "value":{
        "2021-12-17T03:00:00.000Z":3377.42,
        "2021-12-17T04:00:00.000Z":3377.42
    }
}
```