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
	request_json = request.get_json()
	# ajouter les données dans la bdd
	print(request_json)
	# retourner un status
	return {"status": "OK"}