import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.config import db
from app.models.main import User
from app.forms.main import UserForm

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/convocatoria', methods=['GET','POST'])
def convocatoria():
    form = UserForm()
    if form.validate_on_submit():
        # Guardar archivos subidos
        upload_folder = current_app.config['UPLOAD_FOLDER']
        tarjeton_pago_filename = secure_filename(form.tarjeton_pago.data.filename)
        form.tarjeton_pago.data.save(os.path.join(upload_folder, tarjeton_pago_filename))

        licencia_manejo_filename = secure_filename(form.licencia_manejo.data.filename)
        form.licencia_manejo.data.save(os.path.join(upload_folder, licencia_manejo_filename))

        tarjeta_circulacion_filename = secure_filename(form.tarjeta_circulacion.data.filename)
        form.tarjeta_circulacion.data.save(os.path.join(upload_folder, tarjeta_circulacion_filename))

        # Crear objeto User
        usuario = User(
            matricula=form.matricula.data,
            nombres=form.nombres.data,
            apellido_paterno=form.apellido_paterno.data,
            apellido_materno=form.apellido_materno.data,
            telefono=form.telefono.data,
            correo_electronico=form.correo_electronico.data,
            antiguedad_anos=form.antiguedad_anos.data,
            antiguedad_quincenas=form.antiguedad_quincenas.data,
            antiguedad_dias=form.antiguedad_dias.data,
            dias_descanso=','.join(form.dias_descanso.data),
            placas=form.placas.data,
            marca_vehiculo=form.marca_vehiculo.data,
            modelo_vehiculo=form.modelo_vehiculo.data,
            tarjeton_pago=tarjeton_pago_filename,
            licencia_manejo=licencia_manejo_filename,
            tarjeta_circulacion=tarjeta_circulacion_filename
        )

        # Guardar en la base de datos
        db.session.add(usuario)
        db.session.commit()

        flash('Registro exitoso', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('convocatoria.html',form=form)