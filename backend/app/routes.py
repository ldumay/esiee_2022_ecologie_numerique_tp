# Fichier Routes
from flask import request, redirect
from app import app, db
from app.models import Vent
from app.controllers import ControllerVent

@app.get("/data")
def get_data():
	# retourner les données
	temp = calcul_temp(60, 16, 500, 4)
	return {
		"status": "OK",
		"temp": temp
	}

@app.post("/data")
def post_data():
	# Recup les données dans le post
	request_arg = request.args
	request_form = request.form
	# ajouter les données dans la bdd
	# retourner un status
	return {
		"status": "OK",
		"test":  {
			"url_arg": request_arg,
			"form_arg": request_form,
		}
	}

@app.get("/test")
def get_test():
	temp_cable = request.args.get('temp_cable', type=int) or request.form.get('temp_cable', type=int) or 24
	temp_ambiant = request.args.get('temp_ambiant', type=int) or request.form.get('temp_ambiant', type=int) or 16
	intensity = request.args.get('intensity', type=int) or request.form.get('intensity', type=int) or 500
	wind_speed = request.args.get('wind_speed', type=int) or request.form.get('wind_speed', type=int) or 4
	temp = calcul_temp(temp_cable, temp_ambiant, intensity, wind_speed)
	return { "value": temp }

def calcul_temp(temperature_cable: int, temperature_ambiant: int, intensity: int, wind_speed: int):
	# Retourne le calcul de la température
	part1 = ((wind_speed * wind_speed) / 1600) * 0.4 - 0.1
	part2 = (temperature_cable - temperature_ambiant - ((pow(intensity, 1.4) / 73785) * 130))

	temperature_total = part1 * part2

	return temperature_total



# - - - - - - [Exemple de gestion de méthodes] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route('/sample_methodes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sample_methodes():
    if request.method=='GET':
        return "Cet méthode est un GET 😉👌"
    elif request.method=='POST':
        return " Cet méthode est un GET 😉👌"
    elif request.method=='PUT':
        return " Cet méthode est un PUT 😉👌"
    elif request.method=='DELETE':
        return " Cet méthode est un DELETE 😉👌"
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"

# - - - - - - [BDD] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GET - Récupération du contenu de la BDD
@app.get("/bdd")
def datas_all():
    if request.method=='GET':
        return ControllerVent.all
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"

@app.post('/bdd/create')
def datas_create():
    if request.method=='POST':
        heure = request.form.get('heure')
        intencite = request.form.get('intencite')
        temperature = request.form.get('temperature')
        vitesse = request.form.get('vitesse')
        return ControllerVent.create(heure, intencite, temperature, vitesse)
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"

@app.put('/bdd/update/<int:id>')
def datas_update(id):
    if request.method=='PUT':
        form = request.form
        heure = form.get('heure')
        intencite = form.get('intencite')
        temperature = form.get('temperature')
        vitesse = form.get('vitesse')
        return ControllerVent.update(id, heure, intencite, temperature, vitesse)
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"

@app.delete('/bdd/delete/<int:id>')
def datas_delete(id):
    if request.method=='PUT':
        return ControllerVent.delete(id)
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"