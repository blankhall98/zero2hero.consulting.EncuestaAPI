from flask import Flask

def create_app():

    app = Flask(__name__)

    # Register the main blueprint
    from app.main.main import main
    app.register_blueprint(main)

    # Register the admin blueprint
    from app.admin.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    return app