# Flask
from flask import Flask, request
# Datetime
from datetime import datetime
# Regex
import re

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello World"

@app.route("/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.get("/data")
def get_data():
	# recup les données de la bdd
	# retourner les données
	return {"status": "OK"}

@app.post("/data")
def post_data():
	# Recup les données dans le post
	request_arg = request.args
	request_form = request.form
	# ajouter les données dans la bdd
	# retourner un status
	return {"status": "OK", "test":  {
		"url_arg": request_arg,
		"form_arg": request_form,
		}
	}

@app.get("/test")
def get_test():
	temp_cable = request.args.get('temp')
	if (temp_cable):
		temp = calcul_temp(temp_cable)
	else:
		temp = calcul_temp(24)
	return { "value": temp }

def calcul_temp(temperature_cable: int):
	# Récupèrer les dernières informations stockés dans la bdd
	# 
	#
	wind_speed = 10
	temperature_ambiant = 16
	intensity = 500

	part1 = ((wind_speed * wind_speed) / 1600) * 0.4 - 0.1
	part2 = (temperature_cable - temperature_ambiant - ((pow(intensity, 1.4) / 73785) * 130))

	temperature_total = part1 * part2

	return temperature_total