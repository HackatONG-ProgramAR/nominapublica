from app import db
from sqlalchemy.dialects.postgresql import JSON


class Persona(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)