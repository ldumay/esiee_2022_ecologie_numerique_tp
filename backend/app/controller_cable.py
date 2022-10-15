# Fichier - Controlle - Cable
from .model_cable import Cable

from app.bdd_sqlite_manager import BddSQLiteManager

# Entité - Cable
class ControllerCable:
	
	# Constructeur
	def __init__(self, manager: BddSQLiteManager):
		super().__init__()
		self.BDDmanager = manager

	# Méthode de récupération de toutes les données
	def getAll(self):
		result = self.BDDmanager.getAllCable()
		if (result) or (len(result) > 0):
			return result
		else:
			return "[Cable-All] - Il n'y a pas de données dans la BDD."

	# Méthode de récupération d'une donnée
	def getCable(self, id: int):
		result = self.BDDmanager.getCable(id)
		if result:
			return result
		else:
			return "[Cable-Get] - La donnée n'a pas été trouvée dans la BDD."

	# Méthode de création d'une donnée
	def create(self, temperature_cable, temperature_ambiant, intensity, wind_speed):
		try:
			result = self.BDDmanager.insertCable(temperature_cable, temperature_ambiant, intensity, wind_speed)
			if result:
				return "[Cable-Create] - La donnée a bien été ajoutée dans la BDD."
			else:
				return "[Cable-Create] - La donnée n'a pas été ajoutée dans la BDD."
		except:
			return "[Cable-Create] - Error"

	# Méthode de mise à jour d'une donnée
	def update(self, id, temperature_cable, temperature_ambiant, intensity, wind_speed):
		result = self.BDDmanager.updateCable(id, temperature_cable, temperature_ambiant, intensity, wind_speed)
		if result:
			return "[Cable-Update] - La donnée a bien été modifiée dans la BDD."
		else:
			return "[Cable-Update] - La donnée n'a pas été modifiée dans la BDD."

	# Méthode de suppression d'une donnée
	def delete(self, id):
		result = self.BDDmanager.deleteCable(id)
		if result:
			return "[Cable-Delete] - La donnée a bien été supprimée de la BDD."
		else:
			return "[Cable-Delete] - La donnée n'a pas été supprimée de la BDD."
