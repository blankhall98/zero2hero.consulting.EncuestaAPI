from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SelectMultipleField, validators
from flask_wtf.file import FileAllowed
from wtforms.widgets import ListWidget, CheckboxInput

class UserForm(FlaskForm):
    nombres = StringField('Nombres', [validators.DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', [validators.DataRequired()])
    apellido_materno = StringField('Apellido Materno', [validators.DataRequired()])
    telefono = StringField('Teléfono Personal', [validators.DataRequired()])
    correo_electronico = StringField('Correo Electrónico', [validators.DataRequired(), validators.Email()])
    antiguedad_anos = IntegerField('Años', [validators.DataRequired()])
    antiguedad_quincenas = IntegerField('Quincenas', [validators.DataRequired()])
    antiguedad_dias = IntegerField('Días', [validators.DataRequired()])
    matricula = IntegerField('Matrícula Trabajador IMSS', [validators.DataRequired()])
    dias_descanso = SelectMultipleField('Días de Descanso', choices=[
        ('lunes', 'Lunes'), ('martes', 'Martes'), ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sábado', 'Sábado'),
        ('domingo', 'Domingo')
    ], option_widget=CheckboxInput(), widget=ListWidget(prefix_label=False)) # Usar casillas de verificación
    placas = StringField('Placas del Vehículo', [validators.DataRequired()])
    marca_vehiculo = StringField('Marca del Vehículo', [validators.DataRequired()], 
                                 render_kw={"placeholder": "Ejemplo: Toyota"})
    modelo_vehiculo = StringField('Modelo Específico del Vehículo', [validators.DataRequired()], 
                                  render_kw={"placeholder": "Ejemplo: Corolla 2020"})
    tarjeton_pago = FileField('Tarjetón de Pago', validators=[FileAllowed(['pdf'], 'Sólo se permiten archivos PDF')])
    licencia_manejo = FileField('Licencia de Manejo', validators=[FileAllowed(['pdf'], 'Sólo se permiten archivos PDF')])
    tarjeta_circulacion = FileField('Tarjeta de Circulación', validators=[FileAllowed(['pdf'], 'Sólo se permiten archivos PDF')])