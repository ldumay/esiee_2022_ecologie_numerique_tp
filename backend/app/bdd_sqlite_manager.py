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
		except Error as err:
			print('[BDD] Error !')
			print(err)

		# Insertion des données la table Cable de la BDD
		try:
			new_vent_1 = """INSERT INTO cable 
				(temperature_cable, temperature_ambiant, intensity, wind_speed)
				VALUES
				(0, 0, 0, 0)
			"""
			self.bdd.getExecute(new_vent_1)
			print("[BDD] Insertion dans la table CABLE - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

		# Lecture des données de la table Cable de la BDD
		try:
			query = "SELECT * FROM cable"
			print(self.bdd.getAll(query))
			print("[BDD] Lecture de la table CABLE - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)
		
		# Lecture du dernier enregistrement de la table Cable de la BDD
		try:
			result = self.getLastAddedCable()
			print(result)
			print("[BDD] Lecture du dernier enregistrement de la table CABLE - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

		#Lecture du nombre d'enregistrement de la table Cable de la BDD
		try:
			result = self.getNumberCable()
			print(result)
			print("[BDD] Lecture du nombre d'enregistrement de la table CABLE - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

	def getBDD(self):
		return self.bdd
	
	def getAllCable(self):
		query = "SELECT * FROM cable"
		result = self.getBDD().getAll(query=query)
		return result
	
	def getCable(self, id: int):
		query = "SELECT * FROM cable WHERE id = {}".format(id)
		# print(query, flush=True)
		result = self.getBDD().getOnce(query=query)
		return result
	
	def getLastAddedCable(self):
		query = "SELECT * FROM cable ORDER BY id DESC LIMIT 1"
		result = self.getBDD().getOnce(query=query)
		return result
	
	def getNumberCable(self):
		query = "SELECT COUNT(*) as number FROM cable"
		result = self.getBDD().count(query=query)
		return result

	def insertCable(self, temp_cable: float, temp_amb: float, intensity: int, wind_speed: float):
		query = """INSERT INTO cable
			(temperature_cable, temperature_ambiant, intensity, wind_speed)
			VALUES
			({}, {}, {}, {})
		""".format(temp_cable, temp_amb, intensity, wind_speed)
		result = self.getBDD().getExecute(query=query)
		return result

	def updateCable(self, id: int, temp_cable: float, temp_amb: float, intensity: int, wind_speed: float):
		query = """UPDATE cable
			SET temperature_cable = {}, temperature_ambiant = {}, intensity = {}, wind_speed = {}
			WHERE id = {}""".format(temp_cable, temp_amb, intensity, wind_speed, id)
		result = self.getBDD().getExecute(query=query)
		return result

	def deleteCable(self, id: int):
		query = """DELETE FROM cable WHERE id = {}""".format(id)
		result = self.getBDD().getExecute(query=query)
		return result
