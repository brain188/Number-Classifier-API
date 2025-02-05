from flask import Flask
from app.middleware import middleware_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(middleware_blueprint)
    return app
