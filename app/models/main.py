from app.config import db

class User(db.Model):
    __tablename__ = 'users'

    ### INFORMACIÓN DEL USUARIO ###
    #Matricula de trabajador IMSS
    matricula = db.Column(db.Integer, primary_key=True)
    #Nombres del trabajador
    nombres = db.Column(db.String(150), nullable=False)
    #Apellido paterno del trabajador
    apellido_paterno = db.Column(db.String(150), nullable=False)
    #Apellido materno del trabajador
    apellido_materno = db.Column(db.String(150), nullable=True)
    #Telefono del trabajador
    telefono = db.Column(db.String(15), nullable=False)
    #Correo electronico del trabajador
    correo_electronico = db.Column(db.String(150), nullable=False, unique=True)
    #Antiguedad del trabajador
    antiguedad_anos = db.Column(db.Integer, nullable=False)
    antiguedad_quincenas = db.Column(db.Integer, nullable=False)
    antiguedad_dias = db.Column(db.Integer, nullable=False)
    #Dias de descanso del trabajador
    dias_descanso = db.Column(db.String(200), nullable=True)

    ### INFORMACIÓN DEL VEHICULO ###
    #Placas del vehiculo
    placas = db.Column(db.String(10), nullable=False)
    #Marca del vehiculo
    marca_vehiculo = db.Column(db.String(100), nullable=False)
    #Modelo del vehiculo
    modelo_vehiculo = db.Column(db.String(100), nullable=False)
    #Tarjeton de pago [PDF]
    tarjeton_pago = db.Column(db.String(200), nullable=False)
    #Licencia de manejo [PDF]
    licencia_manejo = db.Column(db.String(200), nullable=False)
    #Tarjeta de circulación [PDF]
    tarjeta_circulacion = db.Column(db.String(200), nullable=False)