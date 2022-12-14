from forum_app import *
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "login"

@loginManager.user_loader
def load_user(username: db.String):
    '''
    Loads a user using their username.
    '''

    return User.query.get(username)

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
    Logs the user out and returns them to teh login page.
    '''

    logout_user()
    return render_template("login.html", loggedOut=True)