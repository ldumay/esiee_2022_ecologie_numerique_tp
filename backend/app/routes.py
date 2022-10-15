# Fichier Routes
from flask import request, redirect
from app import app
from flask import request

from app.calcul_temp import calcul_temp_minutes, calcul_scipy_temp


# from app.models import Vent
# from app.controllers import ControllerVent
@app.route('/testapps', methods=['GET', 'POST'])
def home():
    return "Hello, welcome to the apps"


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


@app.get("/test")
def get_test():
    test = calcul_scipy_temp(10, 0, 16, 200, 4)
    return {"test": test}


# - - - - - - [Exemple de gestion de méthodes] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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


# - - - - - - [BDD] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GET - Récupération du contenu de la BDD
@app.get("/bdd")
def datas_all():
    if request.method == 'GET':
        result = ''
        # result = ControllerVent.all()
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


@app.post('/bdd/create')
def datas_create():
    if request.method == 'POST':
        heure = request.form.get('heure')
        intencite = request.form.get('intencite')
        temperature = request.form.get('temperature')
        vitesse = request.form.get('vitesse')
        result = ''
        # result = ControllerVent.create(heure, intencite, temperature, vitesse)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


@app.put('/bdd/update/<int:id>')
def datas_update(id):
    if request.method == 'PUT':
        form = request.form
        heure = form.get('heure')
        intencite = form.get('intencite')
        temperature = form.get('temperature')
        vitesse = form.get('vitesse')
        result = ''
        # result = ControllerVent.update(id, heure, intencite, temperature, vitesse)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"


@app.delete('/bdd/delete/<int:id>')
def datas_delete(id):
    if request.method == 'PUT':
        result = ''
        # result = ControllerVent.delete(id)
        return result
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"
