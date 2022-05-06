from bookmarks.ext.flask_sqlalchemy import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    user_type = db.Column(db.Boolean, nullable=False, default=False)
    gender = db.Column(db.String(20), nullable=False)
    ssn = db.Column(db.String(20), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String, nullable=False)
    number = db.Column(db.String(10))
    district = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr(self) -> str:
        return 'User>>> {self.username}'