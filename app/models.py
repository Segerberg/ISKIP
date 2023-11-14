from app import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import SignatureExpired, BadSignature
from itsdangerous.url_safe import URLSafeTimedSerializer
from flask_login import UserMixin
from app import login
import uuid


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    confirmed = db.Column(db.Boolean(), nullable=False, default=False)
    password_hash = db.Column(db.String(128))
    surveys = db.relationship('Survey', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_mail_confirm_token(self):
        s = URLSafeTimedSerializer(
            current_app.config["SECRET_KEY"], salt="email-confirm"
        )
        return s.dumps(self.email, salt="email-confirm")  # todo env

    @staticmethod
    def verify_mail_confirm_token(token):
        try:
            s = URLSafeTimedSerializer(
                current_app.config["SECRET_KEY"], salt="email-confirm"
            )
            email = s.loads(token, salt="email-confirm", max_age=3600)
            return email
        except (SignatureExpired, BadSignature):
            return None

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Survey(db.Model):
    id = db.Column(db.String,primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(128), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    active = db.Column(db.Boolean)
    type = db.Column(db.String(128)) # branch
    created = db.Column(db.DateTime)
    no_participants = db.Column(db.Integer)
    responses = db.relationship('Response', backref='survey', lazy='dynamic')

    def __repr__(self):
        return self.name

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    created = db.Column(db.DateTime)
    data = db.Column(db.JSON)



