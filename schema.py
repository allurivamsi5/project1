from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class schema(db.Model):
    __tablename__ = "schema"
    email = db.Column(db.String, primary_key = True)
    city = db.Column(db.String, nullable = False)
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    time_stamp = db.Column(db.DateTime(timezone = True), nullable = False)


    def __init__(self, email, city, username, password):
        self.email = email
        self.city = city
        self.username = username
        self.password = password
        self.time_stamp = datetime.now()

