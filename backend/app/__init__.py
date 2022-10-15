# Fichier Init

from app.bdd_sqlite_manager import BddSQLiteManager
from app.controller_cable import ControllerCable
from flask import Flask

# Application
app = Flask(__name__)


# - - - [BDD] - - - - - - -

# Initialisation du mananger de la BDD
bdd = BddSQLiteManager()

cable = ControllerCable(bdd)

# - - - [Routes] - - - - - - -
# Gestion des routes
from app import routes
