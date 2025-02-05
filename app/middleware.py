from flask import Blueprint
from app.routes import classify_blueprint

middleware_blueprint = Blueprint('middleware', __name__)

@middleware_blueprint.route('/')
def home():
    return {"message": "Welcome to the Number Classification API"}


middleware_blueprint.register_blueprint(classify_blueprint, url_prefix='/api')
