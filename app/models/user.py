from app.extensions.extensions import db, bcrypt
import random

def generate_random_id():
    return random.randint(10**9, 10**10 - 1)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True, default=generate_random_id, autoincrement=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(self, email, password, confirmed=False):
        self.email = email
        self.set_password(password)
        self.confirmed = confirmed

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
