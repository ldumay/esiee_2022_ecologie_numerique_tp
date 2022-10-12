# Fichier Routes

from app import app
from flask import request

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

	temp_cable = request.args.get('temp_cable', type=int) or request.form.get('temp_cable', type=int)
	temp_ambiant = request.args.get('temp_ambiant', type=int) or request.form.get('temp_ambiant', type=int)
	intensity = request.args.get('intensity', type=int) or request.form.get('intensity', type=int)
	wind_speed = request.args.get('wind_speed', type=int) or request.form.get('wind_speed', type=int)
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
	temp_cable = request.args.get('temp_cable', type=int) or request.form.get('temp_cable', type=int) or 0
	temp_ambiant = request.args.get('temp_ambiant', type=int) or request.form.get('temp_ambiant', type=int) or 16
	intensity = request.args.get('intensity', type=int) or request.form.get('intensity', type=int) or 200
	wind_speed = request.args.get('wind_speed', type=int) or request.form.get('wind_speed', type=int) or 4

	temp_table = []

	# calcul sur les 30 prochaines minutes
	for minute in range(1, 30):
		temp_cable = calcul_temp_minute(temp_cable, temp_ambiant, intensity, wind_speed)
		print({'time': minute, 'temp': temp_cable}, flush=True)
		temp_table.append(temp_cable)
		# line test : intensity + 100 par min
		intensity += 100

	return {"table": temp_table}

def calcul_temp_minute(temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float):
	# Retourne la température du cable dans une simulation de 1 minute aux paramètres donnés
	for time in range(1, 60):
		temperature_cable += calcul_temp(temperature_cable, temperature_ambiant, intensity, wind_speed)
	return temperature_cable

def calcul_temp(temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float) -> float:
	# Retourne le calcul de la température
	# formule de chauffe du cable toutes les secondes selon les paramètres donnés
	# temperature_cable doit etre la temperature de la dernière itération de la formule
	# wind speed en m/s
	# demander pour code carbon
	part1 = ((wind_speed * wind_speed) / 1600) * 0.4 - 0.1
	part2 = (temperature_cable - temperature_ambiant - ((pow(intensity, 1.4) / 73785) * 130))

	temperature_total = part1 * part2

	return temperature_total
