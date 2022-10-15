# Fichier Routes
from app import app, cable
from flask import request, redirect
import jsonpickle
from app.calcul_temp import calcul_temp_minutes, calcul_scipy_temp
from app.model_cable import Cable
from app.controller_cable import ControllerCable

import numpy as np
from werkzeug.debug import console


# - - - [Test] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# from app.models import Vent
# from app.controllers import ControllerVent
@app.route('/testapps', methods=['POST'])
def home():
    data = request.get_json()
    listData = list(data)

    return jsonpickle.encode(listData)


# - - - [Data] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Récupération des données
@app.get("/data")
def get_data():
    minutes = request.args.get('time', type=int) or request.form.get('time', type=int) or 30
    temp_cable = request.args.get('temp_cable', type=int) or request.form.get('temp_cable', type=int) or 0
    temp_ambiant = request.args.get('temp_ambiant', type=int) or request.form.get('temp_ambiant', type=int) or 16
    intensity = request.args.get('intensity', type=int) or request.form.get('intensity', type=int) or 200
    wind_speed = request.args.get('wind_speed', type=int) or request.form.get('wind_speed', type=int) or 4

    # calcul sur les 30 prochaines minutes
    temp = calcul_temp_minutes(minutes, temp_cable, temp_ambiant, intensity, wind_speed)

    return {"temperature": temp}


# Envoyer de données
@app.post("/data")
def post_data():
    # Recup les données dans le post
    request_arg = request.args
    request_form = request.form

    temp_cable = request.args.get('temp_cable', type=int) or request.form.get('temp_cable', type=int)
    temp_ambiant = request.args.get('temp_ambiant', type=int) or request.form.get('temp_ambiant', type=int)
    intensity = request.args.get('intensity', type=int) or request.form.get('intensity', type=int)
    wind_speed = request.args.get('wind_speed', type=int) or request.form.get('wind_speed', type=int)
    # ajouter les données dans la bdd
    # retourner un status
    return {
        "status": "OK",
        "test": {
            "url_arg": request_arg,
            "form_arg": request_form,
        }
    }


# - - - [Exemple de gestion de méthodes] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Exemple de gestion de méthodes
@app.route('/sample_methodes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sample_methodes():
    if request.method == 'GET':
        return "Cet méthode est un GET 😉👌"
    elif request.method == 'POST':
        return " Cet méthode est un GET 😉👌"
    elif request.method == 'PUT':
        return " Cet méthode est un PUT 😉👌"
    elif request.method == 'DELETE':
        return " Cet méthode est un DELETE 😉👌"
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


# - - - [Cable] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GET - Récupération du contenu de la table Cable
@app.get("/cables")
def getCables():
    if request.method == 'GET':
        result = ''
        result = cable.getAll()
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


# GET - Récupération du contenu cable de la table Cable
@app.get("/cable/<int:id>")
def getCable(id):
    if request.method == 'GET':
        result = ''
        result = cable.getCable(id)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


# POST - Création d'un contenu cable et ajout dans la table Cable
@app.post('/bdd/create')
def createCable():
    if request.method == 'POST':
        data = request.get_json()
        listData = list(data)

        temperature_cable = request.form.get('temperature_cable')
        temperature_ambiant = request.form.get('temperature_ambiant')
        intensity = request.form.get('intensity')
        wind_speed = request.form.get('wind_speed')
        result = cable.create(temperature_cable, temperature_ambiant, intensity, wind_speed)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


# PUT - Mise à jour d'un contenu cable dans la table Cable
@app.put('/bdd/update/<int:id>')
def updateCable(id):
    if request.method == 'PUT':
        temperature_cable = request.form.get('temperature_cable')
        temperature_ambiant = request.form.get('temperature_ambiant')
        intensity = request.form.get('intensity')
        wind_speed = request.form.get('wind_speed')
        result = ''
        result = cable.update(id, temperature_cable, temperature_ambiant, intensity, wind_speed)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


# DELETE - Supprimer d'un contenu cable dans la table Cable
@app.delete('/bdd/delete/<int:id>')
def deleteCable(id):
    if request.method == 'PUT':
        result = ''
        result = cable.delete(id)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"
