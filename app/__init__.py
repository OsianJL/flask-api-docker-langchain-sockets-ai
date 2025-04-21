from flask import Flask
from app.config.config import Config
from app.extensions.extensions import db, jwt, migrate, bcrypt

from app.models.user import User
from flask import request, jsonify

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Simple health check route
    @app.route('/')
    def hello():
        return {'message': 'API is running'}, 200
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered"}), 409

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201


    from app.models import user  # Import models to register them
    
    
    return app
