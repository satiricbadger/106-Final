
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
from flask import abort, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
import sys
import json

app = Flask(__name__)
app.secret_key = 'super secret key'

with app.app_context():
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="ansony3",password="testpack",hostname="ansony3.mysql.pythonanywhere-services.com",databasename="ansony3$forum_db_dec6",)
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    db = SQLAlchemy(app)


    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        userID = db.Column(db.String(500), unique=True, nullable=False)
        password = db.Column(db.String(500), unique=False, nullable=False)

    class forumID(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        tag = db.Column(db.String(500), unique = True, nullable = False)

    class ForumPost(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        userID = db.Column(db.String(500), unique=False, nullable=False) #This is to mark who is the original poster.
        text = db.Column(db.String(500),nullable = False) #This is where the text post is....
        tag = db.Column(db.String(500), nullable = False) #This is to set what tag the post could be.
        time = db.Column(db.String(500),nullable = False) #This is to show the time the post was made?
        score = db.Column(db.String(500), nullable = True) #This is to show upvote or downvotes.

    class ForumReply(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        userID = db.Column(db.String(500), unique=False, nullable=False) #This is to mark who is the original poster.
        text = db.Column(db.String(500),nullable = False) #This is where reply should be
        tag = db.Column(db.String(500), nullable = False) #This is to set what tag the post could be. This could be optional.
        time = db.Column(db.String(500),nullable = False) #This is to show the time the post was made?
        score = db.Column(db.Integer, nullable = True) #This shows upvote and downvote.
        recipient = db.Column(db.String(500), nullable = False) #This should show the person you are replying to

    #Initialize database and classes
    db.create_all()
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(ForumPost, db.session))
    admin.add_view(ModelView(ForumReply, db.session))
    admin.add_view(ModelView(forumID,db.session))




    #Routing of website routes are below.
    @app.route('/')#Login page
    def login():
        return "login page here"




    @app.route('/register') #Show register page
    def register():
        return "register page here"

    @app.route('/anime')
    def anime():
        #Queue all posts in with the anime tag.
        return "anime forum page"

    @app.route('/games')
    def games():
        #Queue all posts in with the games tag-
        return "game forum page"

    #USER FUNCTIONS

    #Allow user to make a post on a forum board.
    #When sending an AJAX request, please send in: username: , text: , tags:
    @app.route('/<string:username>/<string:forum>/post', methods = ['GET','POST'])
    def PostOnForum(username,forum):
        #Query all users & content from the post method.
        contents = request.get_json(silent=True)
        userPost = Users.query.all()
        #Find if this is a valid user so they can post.
        result = db.session.execute(db.select(Users.userID).where(Users.userID == username))
        #If the username from result matches the username argument, allow them to post
        if(result.first().userID == username):
            #Start the post operation.
            #Create new forum thread/post using the ForumPost class.
            db.session.add(ForumPost(userID = contents["username"], text = contents["text"], tag = "none", time = datetime.now(), score = 0))
            #Commit to forum's database.
            db.session.commit()


        return ""

    #Show all posts.
    @app.route('/showAllPosts', methods = ['GET'])
    def getAllPosts():
        allPosts = ForumPost.query.all()
        posts = {}
        for i in allPosts:
            posts[i.id] = i.text
        return posts

    #Show all threads -> This is just making a new link, showing the post, and then including the ability to make a forumReply
    @app.route('/thread/<string:id>')
    def threads(id):
        #Render the html and call the post id?
        #------------actual function below-------------------#
        #Get the id of ForumPost that matches the id in the route. /thread/1 would load up the page with the first post.
        threadPost = db.session.execute(db.select(ForumPost.text).where(ForumPost.id == id))
        #ChunkedIterator is a pain, so we convert it into a dictionary.
        threadDictionary = [dict(r) for r in threadPost.all()]
        #Iterate
        for threadDict in threadDictionary:
            threadDict["text"]
        return threadDict["text"]


    #In the thread, you can call this method to pull up the replies in each of the threads.


    #Allow user to reply to a post.

    #Allow user to upvote a post



