from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

from app import views, models
