# Fichier Init

import os, re, sqlite3
from datetime import datetime
from flask import Flask, request, session
from sqlite3 import Error

from backend.app.managerbddsqlite import ManagerBddSQLite
from backend.app.config import Config

# Application
app = Flask(__name__)
# secret key for cookies


# Configuration de l'application
app.config["DEBUG"] = True
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'dnjqkndkjsndjsdksqshfibvdhhjbsui'

# - - - [BDD] - - - - - - -

# Init BDD
bdd = ManagerBddSQLite()

# Connexion BDD
bdd.connection()

# Check BDD
try:
    table_vent = """CREATE TABLE IF NOT EXISTS vent(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        temperature_cable FLOAT,
        temperature_ambiant FLOAT,
        intensity FLOAT,
        wind_speed FLOAT
    )"""
    bdd.getExecute(table_vent)
    print("[BDD] Vérification de la table - OK !")
except Error as e:
    print('[BDD] Error !')
    print(e)

# Insert - One Data
try:
    new_vent_1 = """INSERT INTO vent 
        (temperature_cable, temperature_ambiant, intensity, wind_speed)
        VALUES
        (0, 0, 0, 0)
    """
    bdd.getExecute(new_vent_1)
    print("[BDD] Insertion dans la table - OK !")
except Error as e:
    print('[BDD] Error !')
    print(e)

# Close
bdd.close()

# - - - [BDD] - - - - - - -

# Rajout des anciens import pour éviter les messages d'erreur sur beaucoup d'autre fichier
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Routes
from backend.app import routes
