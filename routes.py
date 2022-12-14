from forum_app import *

from flask_login import current_user, login_required

@app.route("/", methods=["GET"])
def index():
    '''
    Redirects to app if user is logged in, redirects to login if not. 
    '''

    if current_user.is_authenticated:
        return redirect(url_for("app"))
    
    return redirect(url_for("signin"))

@app.route("/signin", methods=["GET"])
def signin():
    '''
    Display the sign-in page.
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
