from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

from app import views, models
