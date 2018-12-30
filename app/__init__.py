import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate#
from flask_login import LoginManager

#
app = Flask(__name__)
app.config.from_object(Config)
engine = create_engine(os.getenv("DATABASE_URL"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'



from app import routes, models
