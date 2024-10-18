from flask import Blueprint, render_template, current_app, send_from_directory
from app.config import db
from app.models.main import User
import os

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
def admin_index():
    return 'Página de Administración'

@admin.route('/users')
def view_users():
    # Obtener todos los usuarios de la base de datos
    users = User.query.all()
    return render_template('users.html', users=users)

@admin.route('/download/<filename>')
def download_file(filename):
    # Ruta para descargar archivos subidos
    uploads_dir = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads_dir, filename, as_attachment=True)