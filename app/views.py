import json
import time

from flask import request

from . import app  # , db
# from app.models import PR


@app.route('/trade/', methods=['GET', 'POST'])
def trade():
    return "Hello World!"
