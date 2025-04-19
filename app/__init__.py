from flask import Flask
from app.config.config import Config
from app.extensions.extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Simple health check route
    @app.route('/')
    def hello():
        return {'message': 'API is running'}, 200

    return app
