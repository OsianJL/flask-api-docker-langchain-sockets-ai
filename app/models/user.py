from app.extensions.extensions import db
import random

def generate_random_id():
    return random.randint(10**9, 10**10 - 1)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, default=generate_random_id)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
