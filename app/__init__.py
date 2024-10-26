from app.config import app, Config, db, migrate, login_manager
from app.models.admin import Admin

def create_app():

    # Initialize the app
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize the login manager
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))
    
    with app.app_context():
        admin = Admin.query.filter_by(username='admin').first()
        if not admin:
            admin = Admin(username='admin')
            admin.set_password('secret')
            db.session.add(admin)
            db.session.commit()
        print("Initial admin user created")

    # Register the main blueprint
    from app.main.main import main
    app.register_blueprint(main)

    # Register the admin blueprint
    from app.admin.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    return app