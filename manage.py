from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db
from app import Persona
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

import csv

@manager.command
def readCsv(filename):
	print 'importing', filename
	with open(filename, 'r') as aFile:
		reader = csv.DictReader(aFile)
		for row in reader:
			print row['fullname']
			persona = Persona(apellido=row)
			db.session.add(persona)
	db.session.commit()
	print 'importing'

if __name__ == '__main__':
    manager.run()
