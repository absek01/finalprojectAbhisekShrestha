import os
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))
    app.config.from_object("config.Config")

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app