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



# - - - - - - [BDD] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.post("/bdd")
def datas_all():
    return ControllerVent.all

@app.route('/bdd/create', methods=['POST'])
def datas_create():
    form = request.form
    heure = form.get('heure')
    intencite = form.get('intencite')
    temperature = form.get('temperature')
    vitesse = form.get('vitesse')
    return ControllerVent.create(heure, intencite, temperature, vitesse)

@app.route('/bdd/update/<int:id>', methods=['POST'])
def datas_update(id):
    form = request.form
    heure = form.get('heure')
    intencite = form.get('intencite')
    temperature = form.get('temperature')
    vitesse = form.get('vitesse')
    return ControllerVent.update(id, heure, intencite, temperature, vitesse)


@app.route('/bdd/delete/<int:id>', methods=['POST'])
def datas_delete(id):
    return ControllerVent.delete(id)