from flask import Flask
from app.config.config import Config
from app.extensions.extensions import db, jwt, migrate, bcrypt, socketio
from app.resources.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    socketio.init_app(app) 
    
    app.register_blueprint(auth_bp)

    # Simple health check route
    @app.route('/')
    def hello():
        return {'message': 'API is running'}, 200
    
    
    
    
    return app
