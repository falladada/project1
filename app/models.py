from datetime import datetime
from app import db, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


#Defining the Users_Table
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship("Review", backref="author", lazy='dynamic' )


    # instructions for printing objects of class 'User'
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#Defining the Review Table
class Review (db.Model):
    __tablename__= 'review'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(4000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Review: {}'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
