from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
def admin_index():
    return 'Página de Administración'

@admin.route('/consultas')
def consultas():
    return 'Consultas'