from forum_app.py import *

from flask_login import current_user, login_required

@app.route("/", methods=["GET"])
def index():
    '''
    Redirects to app if user is logged in, redirects to login if not. 
    '''

    if current_user.is_authenticated:
        return redirect(url_for("app"))
    
    return redirect(url_for("login"))

@app.route("/login", methods=["GET"])
def login():
    '''
    Display the login page.
    '''

    if current_user.is_authenticated:
        return redirect(url_for("app"))
    
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register():
    '''
    Display the registration page.
    '''

    if current_user.is_authenticated:
        return redirect(url_for("app"))

    return render_template("register.html")

@app.route("/app", methods=["GET"])
@login_required
def application():
    '''
    Display the application to the user.
    '''

    # This is called 'application' because naming it 'app'
    # will trigger a namespace collision with Flask's 'app'

    return render_template("app.html")