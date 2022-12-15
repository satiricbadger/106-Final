from forum_app import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "login"

import time

@loginManager.user_loader
def load_user(username: str):
    '''
    Loads a user using their username.
    '''

    return User.query.get(username)

@app.route("/register", methods=["POST"])
def signup():
    '''
    Registers the user with their given username and password.
    '''

    if User.signup(request.form["username"], request.form["password"]):
        return redirect(url_for("application"))
    else:
        return render_template("register.html", failed=True)

@app.route("/login", methods=["POST"])
def login():
    '''
    Authenticates the user.
    '''

    time.sleep(2)
    user = User.login(request.form["username"], request.form["password"])

    # User fails to log in, returns to login page
    if user == False:
        return render_template("login.html", failed=True)
    
    # Successful login
    login_user(user)
    return redirect(url_for("application"))

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    '''
    Logs the user out and returns them to the login page.
    '''

    logout_user()
    return render_template("login.html", loggedOut=True)

    
@app.route("/writepost", methods=["POST"])
def writepost():
    '''
    Writes the requested post.
    '''
    Post.createpost(request.form["content"], current_user)
    
    return redirect(url_for("application"))

@app.route("/upvote", methods=["POST"])
def upvote():
    '''
    Upvotes the requested post. Currently, implementation of
    a system that allows the users to upvote only once is
    not possible.
    '''

    postID = request.form["id"]
    post = Post.query.filter_by(id=postID).first()
    post.upvote()
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("application"))