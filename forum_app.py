from flask import *
from flask_sqlalchemy import *

#   Instantiates the app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#admin = Admin(app, name='microblog', template_mode='bootstrap3')

#   Initialize database and classes
db = SQLAlchemy(app)
from models import *
with app.app_context():
    db.create_all()

#   Add routes
from routes import *

#   Add authentication
from auth import *