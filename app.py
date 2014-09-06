from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from models import Persona

@app.route('/')
def hello():
    print db.models.Persona.query.all()
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()