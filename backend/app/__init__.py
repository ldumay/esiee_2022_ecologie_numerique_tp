# OS
import os
# Datetime
from datetime import datetime
# Regex
import re
# Flask - Imports Flask, request
from flask import Flask, request
# BDD - Imports Config, SQLAlchemy, Migrate
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Application
app = Flask(__name__)

# BDD
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models