import os
import sys

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_uri
if app.config['SQLALCHEMY_DATABASE_URI'] is None:
    print("Need database config")
    sys.exit(1)

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
