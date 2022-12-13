import bcrypt
from app import db
from flask_login import UserMixin
from typing import Union

class User(UserMixin, db.Model):
    '''
    Definition for a user. 
    '''

    __tablename__ = 'user'

    #   Define values for a user
    username = db.Column(db.String(256), unique=True, nullable=True)
    password = db.Column(db.String(256), unique=False, nullable=True)

    def __init__(self, username=None, password=None):
        '''
        Constructor for users.
        '''

        self.username = username
        self.password = password

    def login(username: str, password: str) -> Union[User, bool]:
        '''
        Checks if the username and password match.
        '''

        if (((user:=User.query.filter_by(username=username).first()) != None) and bcrypt.checkpw(password.encode(), user.password)):
            return user
        else:
                return false

    #to do: register

class Post(db.Model):
    '''
    Definition for a post.
    '''

    __tablename__ = "post"

    # Define values for a post
    contents    = db.Column(db.String(400), unique=False, nullable=True)
    tags        = db.Column(JSON, nullable=True)
    author      = db.Column(db.String(256), unique=False, nullable=False)
    likes       = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, contents=None, tags=None, author='', likes=0):
        '''
        Constructor for a post
        '''

        self.contents = contents
        self.tags = tags
        self.author = author
        self.likes = likes


