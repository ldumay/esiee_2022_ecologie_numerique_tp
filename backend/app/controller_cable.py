# Fichier - Controlle - Cable
from .model_cable import Cable

# Entité - Cable
class ControllerCable:
	
	# Constructeur
	def __init__(self, bdd):
		super().__init__()
		self.bdd = bdd

	# Méthode de récupération de toutes les données
	@staticmethod
	def getAll(self):
		try:
			query = """SELECT * FROM cable"""
			result = self.bdd.getAll(query)
			if len(result)>0:
				return [ { result } ]
			else:
				return "[Cable-All] - Il n'y a pas de données dans la BDD."
		except:
			return "[Cable-All] - Error"

	# Méthode de récupération d'une donnée
	@staticmethod
	def getCable(self, id):
		try:
			query = """SELECT * FROM cable WHERE id = %s"""
			result = self.bdd.getOnce(query, (id,))
			if result:
				return result
			else:
				return "[Cable-Get] - La donnée n'a pas été trouvée dans la BDD."
		except:
			return "[Cable-Get] - Error"

	# Méthode de création d'une donnée
	@staticmethod
	def create(self, temperature_cable, temperature_ambiant, intensity, wind_speed):
		try:
			query = """INSERT INTO cable
				(temperature_cable, temperature_ambiant, intensity, wind_speed)
				VALUES
				(%s, %s, %s, %s)
			"""
			result = self.bdd.insert(query, (temperature_cable, temperature_ambiant, intensity, wind_speed))
			if result:
				return "[Cable-Create] - La donnée a bien été ajoutée dans la BDD."
			else:
				return "[Cable-Create] - La donnée n'a pas été ajoutée dans la BDD."
		except:
			return "[Cable-Create] - Error"

	# Méthode de mise à jour d'une donnée
	@staticmethod
	def update(self, id, temperature_cable, temperature_ambiant, intensity, wind_speed):
		try:
			query = """UPDATE cable SET temperature_cable = %s, temperature_ambiant = %s, intensity = %s, wind_speed = %s WHERE id = %s"""
			result = self.bdd.update(query, (temperature_cable, temperature_ambiant, intensity, wind_speed))
			if result:
				return "[Cable-Update] - La donnée a bien été modifiée dans la BDD."
			else:
				return "[Cable-Update] - La donnée n'a pas été modifiée dans la BDD."
		except:
			return "[Cable-Update] - Error"

	# Méthode de suppression d'une donnée
	@staticmethod
	def delete(self, id):
		try:
			query = """DELETE FROM cable WHERE id = %s"""
			result = self.bdd.delete(query, (id,))
			if result:
				return "[Cable-Delete] - La donnée a bien été supprimée de la BDD."
			else:
				return "[Cable-Delete] - La donnée n'a pas été supprimée de la BDD."
		except:
			return "[Cable-Delete] - Error"