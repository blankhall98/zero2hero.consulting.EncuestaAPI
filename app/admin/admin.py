from flask import Blueprint, render_template, current_app, send_from_directory, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.config import db
from app.models.main import User
from app.models.admin import Admin
import os

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
def admin_index():
    return redirect(url_for('admin.dashboard'))

#Login
@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')

#logout
@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

#admin dashboard
@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

#view users in database
@admin.route('/users')
@login_required
def view_users():
    # Obtener todos los usuarios de la base de datos
    users = User.query.all()
    return render_template('users.html', users=users)

@admin.route('/download_data')
@login_required
def download_data():
    return render_template('on_work.html')

@admin.route('/view_statistics')
@login_required
def view_statistics():
    return render_template('on_work.html')

#Create admin
@admin.route('/create_admin', methods=['GET', 'POST'])
@login_required
def create_admin():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if username already exists
        existing_admin = Admin.query.filter_by(username=username).first()
        if existing_admin:
            flash('Username already exists. Please choose a different username.', 'warning')
            return redirect(url_for('admin.create_admin'))

        # Create a new admin user
        new_admin = Admin(username=username)
        new_admin.set_password(password)
        
        # Add and commit to the database
        db.session.add(new_admin)
        db.session.commit()
        
        flash('New admin created successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    
    return render_template('create_admin.html')

@admin.route('/download/<filename>')
@login_required
def download_file(filename):
    # Ruta para descargar archivos subidos
    uploads_dir = os.path.join(current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads_dir, filename, as_attachment=True)
