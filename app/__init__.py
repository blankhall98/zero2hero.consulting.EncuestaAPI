from flask import Flask
from app.config import Config, db, migrate

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the main blueprint
    from app.main.main import main
    app.register_blueprint(main)

    # Register the admin blueprint
    from app.admin.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    return app