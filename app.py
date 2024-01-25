from flask import Flask
from main import main as main_blueprint
from auth import auth as auth_blueprint


# to create function for app
def create_app():
    app = Flask(__name__)
    # to register blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app