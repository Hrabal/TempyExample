import locale
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

locale.setlocale(locale.LC_TIME, locale.getlocale())
logging.basicConfig()

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import models
import controllers
