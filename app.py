from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


from sqlalchemy import Float
import json

class Entity(object):
    @property
    def as_dict(self):
        d = {}
        for column in self.__table__.columns:
          attr = getattr(self, column.name)
          if attr is not None:
            if isinstance(column.type, Float):
              d[column.name] = float(attr)
            else:
              d[column.name] = unicode(attr)
          else:
            d[column.name] = None
        return d

class Persona(db.Model, Entity):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer)
    apellido = db.Column(db.String())
    nombres = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route('/api/personas')
def hello():
    personas = [row.as_dict for row in db.session.query(Persona).all()]
    return json.dumps(personas)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
