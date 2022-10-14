# Fichier Init

import os, re, sqlite3
import managerbddsqlite
from datetime import datetime
from sqlite3 import Error
from managerbddsqlite import ManagerBddSQLite
from flask import Flask, request, session
from app.config import Config

# Application
app = Flask(__name__)

# Configuration de l'application
app.config["DEBUG"] = True
app.config.from_object(Config)

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

# Routes
from app import models, routes