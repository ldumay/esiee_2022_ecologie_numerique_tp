# Fichier - Classe - BddSQLiteManager

import sqlite3
from sqlite3 import Error
from app.bdd_sqlite import BddSQLite

class BddSQLiteManager:

	# Constructeur
	def __init__(self):
		# Init BDD
		self.bdd = BddSQLite()

		# Connexion BDD
		self.bdd.connection()

		# Initialisation de la BDD
		self.init()
		
	# Initialisation de la BDD
	def init(self):

		# Vérification de la table Cable dans la BDD
		try:
			table_vent = """CREATE TABLE IF NOT EXISTS cable(
				id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
				temperature_cable FLOAT,
				temperature_ambiant FLOAT,
				intensity FLOAT,
				wind_speed FLOAT
			)"""
			self.bdd.getExecute(table_vent)
			print("[BDD] Vérification de la table CABLE - OK !")
		except Error as e:
			print('[BDD] Error !')
			print(e)

		# Insertion des données la table Cable de la BDD
		try:
			new_vent_1 = """INSERT INTO cable 
				(temperature_cable, temperature_ambiant, intensity, wind_speed)
				VALUES
				(0, 0, 0, 0)
			"""
			self.bdd.getExecute(new_vent_1)
			print("[BDD] Insertion dans la table CABLE - OK !")
		except Error as e:
			print('[BDD] Error !')
			print(e)

		# Lecture des données de la table Cable de la BDD
		try:
			query = "SELECT * FROM cable"
			print(self.bdd.getAll(query))
			print("[BDD] Lecture de la table CABLE - OK !")
		except Error as e:
			print('[BDD] Error !')
			print(e)
		
		# Lecture du dernier enregistrement de la table Cable de la BDD
		try:
			query = "SELECT * FROM cable ORDER BY id DESC LIMIT 1"
			print(self.bdd.getOnce(query))
			print("[BDD] Lecture du dernier enregistrement de la table CABLE - OK !")
		except Error as e:
			print('[BDD] Error !')
			print(e)

		#Lecture du nombre d'enregistrement de la table Cable de la BDD
		try:
			query = "SELECT COUNT(*) as number FROM cable"
			print(self.bdd.count(query))
			print("[BDD] Lecture du nombre d'enregistrement de la table CABLE - OK !")
		except Error as e:
			print('[BDD] Error !')
			print(e)

	def getBDD(self):
		return self.bdd
	
	def getAllCable(self):
		query = "SELECT * FROM cable"
		result = self.getBDD().getAll(query=query)
		return result
	
	def getCable(self, id: int):
		query = "SELECT * FROM cable WHERE id = {id}"
		query.format(id)
		result = self.getBDD().getOnce(query=query)
		return result

	def insertCable(self, temp_cable, temp_amb, intensity, wind_speed):
		query = """INSERT INTO cable
			(temperature_cable, temperature_ambiant, intensity, wind_speed)
			VALUES
			({temp_cable}, {temp_amb}, {intensity}, {wind_speed})
		"""
		query.format(temp_cable, temp_amb, intensity, wind_speed)
		result = self.getBDD().getExecute(query=query)
		return result

	def updateCable(self, id: int, temp_cable, temp_amb, intensity, wind_speed):
		query = """UPDATE cable SET temperature_cable = {temp_cable}, temperature_ambiant = {temp_amb}, intensity = {intensity}, wind_speed = {wind_speed} WHERE id = {id}"""
		query.format(id, temp_cable, temp_amb, intensity, wind_speed)
		result = self.getBDD().getExecute(query=query)
		return result

	def deleteCable(self, id: int):
		query = """DELETE FROM cable WHERE id = {id}"""
		query.format(id)
		result = self.getBDD().getExecute(query=query)
		return result
