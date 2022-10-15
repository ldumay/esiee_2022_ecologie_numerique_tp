# Fichier Init

import os, re, sqlite3
from datetime import datetime
from sqlite3 import Error
from app.bdd_sqlite import BddSQLite
from app.bdd_sqlite_manager import BddSQLiteManager
from flask import Flask, request, session

# Application
app = Flask(__name__)

# Configuration de l'application
app.config["DEBUG"] = True

# - - - [BDD] - - - - - - -

# Initialisation du mananger de la BDD
bdd = BddSQLiteManager()

# - - - [BDD] - - - - - - -

# Rajout des anciens import pour éviter les messages d'erreur sur beaucoup d'autre fichier
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Routes
from app import routes