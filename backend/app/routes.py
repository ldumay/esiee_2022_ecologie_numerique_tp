# Fichier Routes

from app import app
from flask import request

from app.calcul_temp import calcul_temp, calcul_temp_minutes

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

	# calcul sur les 30 prochaines minutes
	temp = calcul_temp_minutes(30, temp_cable, temp_ambiant, intensity, wind_speed)

	return {"temperature": temp}
