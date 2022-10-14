# Fichier Routes

from app import app
from flask import request

from app.calcul_temp import calcul_temp_minutes, calcul_scipy_temp

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
		"test":  {
			"url_arg": request_arg,
			"form_arg": request_form,
		}
	}

@app.get("/test")
def get_test():
	test = calcul_scipy_temp(10, 0, 16, 200, 4)
	return {"test": test}
