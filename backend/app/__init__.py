# Fichier Init

# OS
import os
# Datetime
from datetime import datetime
# Regex
import re
# Flask - Imports Flask, request, session
from flask import Flask, request, session
# BDD - Imports Config, SQLAlchemy, Migrate
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Application
app = Flask(__name__)

# Configuration de l'application
app.config["DEBUG"] = True
app.config.from_object(Config)

# BDD
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Routes
from app import models, routes