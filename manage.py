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

def cleanMoney(dirty):
	return dirty.replace('$', '').replace(',','').strip()

@manager.command
def readCsv(filename):
	print 'importing', filename
	# db.drop_all()
	# db.create_all()

	with open(filename, 'r') as aFile:
		reader = csv.reader(aFile)
		for row in reader:
			fecha = row[0].strip()
			fullname = row[1].strip().decode('utf8')
			bruto = row[2].strip()
			costo = row[3].strip()
			neto = row[4].strip()
			situacion = row[5].strip()

			apellido = fullname.split(' ')[0]
			nombres = ' '.join(fullname.split(' ')[1:])
			sueldoBruto = cleanMoney(bruto)
			year = int(fecha[0:4])
			month = int(fecha[4:])

			print fecha, fullname, apellido, nombres, sueldoBruto

			persona = Persona(apellido=apellido, nombres=nombres)
			sueldo = Sueldo(bruto=float(sueldoBruto), year=year, month=month)
			persona.sueldos.append(sueldo)
			db.session.merge(persona)
			
	db.session.commit()

if __name__ == '__main__':
    manager.run()
