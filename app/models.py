from datetime import datetime
from app import db



#Defining the Users_Table
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship("Review", back_populates="user", lazy='dynamic' )


    # instructions for printing objects of class 'User'
    def __repr__(self):
        return '<User {}>'.format(self.username)


#Defining the Review Table
class Review (db.Model):
    __tablename__= 'review'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(4000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="reviews")


    def __repr__(self):
        return 'Review {}'.format(self.body)
