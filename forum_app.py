from flask import *
from flask_sqlalchemy import *
from flask_admin import *
from flask_login import *
from datetime import datetime
from enum import Enum
from urllib.parse import parse_qs
from urllib.parse import urlparse
import sys
import json

#   Instantiates the app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="ansony3",password="testpack",hostname="ansony3.mysql.pythonanywhere-services.com",databasename="ansony3$forum_db_dec6",)
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

#   Runs the app locally
app.run(host='127.0.0.1', port=5500, debug=True)
