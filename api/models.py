import jwt
from flask import current_app
from datetime import datetime, timedelta
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    email = db.Column(db.String(128), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    records = db.relationship('Record', backref='user')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_jwt(self):
        payload = {
            'user_id': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'])
        return token.decode('unicode_escape')

    @staticmethod
    def parse_jwt(request):
        token = request.headers.get('Authorization').split()[1]
        return jwt.decode(token, current_app.config['SECRET_KEY'])

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date, nullable=False)
    begin_time = db.Column(db.DateTime, index=True, nullable=False)
    finish_time = db.Column(db.DateTime, index=True, nullable=False)
    contents = db.Column(db.String(256), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Record %r %r>' % (self.user_id, self.day)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'day': self.day,
            'begin_time': self.begin_time,
            'finish_time': self.finish_time,
            'contents': self.contents,
            'user_id': self.user_id
        }
