from flask import Flask
from app.config.config import Config
from app.extensions.extensions import db, jwt, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Simple health check route
    @app.route('/')
    def hello():
        return {'message': 'API is running'}, 200


    from app.models import user  # Import models to register them

    
    return app
