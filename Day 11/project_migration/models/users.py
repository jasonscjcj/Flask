# from flask_app import db
from middleware import db

class User(db.Model):
    __tablename__ = 'project_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))


db.create_all()
