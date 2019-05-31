import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'sqlite:///'+os.path.join(basedir, 'db.chunes')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

marshmallow = Marshmallow(app)


DEBUG = True
PORT = 8000

@app.route('/')
def hallo_welt():
  return 'Hallo Welt'

if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)