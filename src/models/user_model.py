
from config import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True ,autoincrement=True)
    first_name = db.Column(db.String(26), nullable=False)
    last_name = db.Column(db.String(26), nullable=False)
    mobile = db.Column(db.String(26), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(26), nullable=False)
