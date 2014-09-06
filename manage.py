from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db
from app import Persona, Sueldo
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
			fullname = row['fullname'].strip().decode('utf8')
			apellido = fullname.split(' ')[0]
			nombres = ' '.join(fullname.split(' ')[1:])
			sueldoBruto = row['sueldo'].replace('$', '').replace(',','').strip()
			print fullname, apellido, nombres, sueldoBruto
			persona = Persona(apellido=apellido, nombres=nombres)
			sueldo = Sueldo(bruto=float(sueldoBruto))
			persona.sueldos.append(sueldo)
			db.session.merge(persona)
			
	db.session.commit()

if __name__ == '__main__':
    manager.run()
