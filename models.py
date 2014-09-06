from app import db


class Persona(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer)
    apellido = db.Column(db.String())
    nombres = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
