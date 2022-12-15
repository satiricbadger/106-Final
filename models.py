from forum_app import db
from flask_login import UserMixin
from typing import Union

class User(UserMixin, db.Model):
    '''
    Definition for a user. 
    '''

    __tablename__ = 'user'

    #   Define values for a user
    id      = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True, nullable=True)
    password = db.Column(db.String(256), unique=False, nullable=True)

    def __init__(self, username=None, password=None):
        '''
        Constructor for users.
        '''

        self.username = username
        self.password = password

    def login(username: str, password: str):
        '''
        Checks if the username and password match.
        '''

        if (((user:=User.query.filter_by(username=username).first()) != None) and (password == user.password)):
            return user
        else:
            return False

    def signup(username: str, password: str) -> bool:
        '''
        Register the user if possible.
        '''

        # Checks if the username is unique and registers user
        try:
            if User.query.filter_by(username=username).first() == None:
                user = User(username, password)
                db.session.add(user)
                db.session.commit()
                return True

        # If registration fails for some reason e.g. non-unique username 
        except:
            return False

        return False


class Post(db.Model):
    '''
    Definition for a post.
    '''

    __tablename__ = "post"

    # Define values for a post
    id          = db.Column(db.Integer, primary_key=True)
    contents    = db.Column(db.String(400), unique=False, nullable=True)
    tags        = db.Column(db.String(256), unique=False, nullable=True)
    author      = db.Column(db.String(256), unique=False, nullable=False)
    likes       = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, contents=None, tags='', author='', likes=0):
        '''
        Constructor for a post.
        '''

        self.contents = contents
        self.tags = tags
        self.author = author
        self.likes = likes

    def createpost(content: str, author: User):
        '''
        Creates a post with the specified content.
        '''

        taglist=''
        if "#anime" in content and "#games" in content:
            taglist = "both"
        elif "#anime" in content:
            taglist = "anime"
        elif "#games" in content:
            taglist = "games"

        try:
            post = Post(contents=content, tags=taglist, author=author.username, likes=0)
            db.session.add(post)
            db.session.commit()
            print(post.tags)
            return post
        
        except:
            return False
        
        return False

    def upvote(self):
        '''
        Raises the like count of a post by 1.
        '''
        self.likes = self.likes + 1
        return self.likes


