from forum_app import *

from flask_login import current_user, login_required

@app.route("/", methods=["GET"])
def index():
    '''
    Redirects to app if user is logged in, redirects to login if not. 
    '''

    if current_user.is_authenticated:
        return redirect(url_for("application"))
    
    return redirect(url_for("signin"))

@app.route("/login", methods=["GET"])
def login_redirect():
    '''
    GET method for login, not to be confused with the POST method.
    Redirects to the sign-in page.
    '''

    return redirect(url_for("signin"))

@app.route("/signin", methods=["GET"])
def signin():
    '''
    Display the sign-in page.
    '''

    if current_user.is_authenticated:
        return redirect(url_for("application"))
    
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register():
    '''
    Display the registration page.
    '''

    if current_user.is_authenticated:
        return redirect(url_for("application"))

    return render_template("register.html")

@app.route("/app", methods=["GET"])
@login_required
def application():
    '''
    Display the application to the user.
    '''

    # Get all the posts.
    posts = [post for post in Post.query.all()][::-1]

    return render_template("app.html", posts=posts)

@app.route("/profile", methods=["GET"])
@login_required
def profile():
    '''
    Display the personal settings page.
    '''

    return render_template("profile.html")

@app.route("/search-anime", methods=["GET"])
@login_required
def search_anime():
    '''
    Display the application to the user with the anime search.
    '''

    # Get all the posts.
    posts = [post for post in Post.query.all() if "anime" in post.tags or "both" in post.tags][::-1]
    return render_template("app.html", posts=posts)

@app.route("/search-games", methods=["GET"])
@login_required
def search_games():
    '''
    Display the application to the user with the games search.
    '''

    # Get all the posts.
    posts = [post for post in Post.query.all() if "games" in post.tags or "both" in post.tags][::-1]

    return render_template("app.html", posts=posts)