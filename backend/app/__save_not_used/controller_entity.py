# Fichier - Controlle - Entity
from app import db
from model_entity import Entity

# Entité - Vent
class ControllerEntity:
	
	def __init__(self, bdd):
		super().__init__()
		self.bdd = bdd

	def getAll(self):
		try:
			query = """SELECT * FROM entity"""
			result = self.bdd.getAll(query)
			if len(result)>0:
				return [ { result } ]
			else:
				return "Il n'y a pas de données dans la BDD."
		except:
			return "[Entity-All] - Error"

	def getEntity(self, id):
		try:
			query = """SELECT * FROM entity WHERE id = %s"""
			result = self.bdd.getOnce(query, (id,))
			if result:
				return result
			else:
				return "La donnée n'a pas été trouvée dans la BDD."
		except:
			return "[Entity-Get] - Error"

	def create(self, name, description, type):
		try:
			query = """INSERT INTO entity (name, description, type) VALUES (%s, %s, %s)"""
			result = self.bdd.insert(query, (name, description, type))
			if result:
				return "La donnée a bien été ajoutée dans la BDD."
			else:
				return "La donnée n'a pas été ajoutée dans la BDD."
		except:
			return "[Entity-Create] - Error"

	def update(self, id, name, description, type):
		try:
			query = """UPDATE entity SET name = %s, description = %s, type = %s WHERE id = %s"""
			result = self.bdd.update(query, (name, description, type, id))
			if result:
				return "La donnée a bien été modifiée dans la BDD."
			else:
				return "La donnée n'a pas été modifiée dans la BDD."
		except:
			return "[Entity-Update] - Error"

	def delete(self, id):
		try:
			query = """DELETE FROM entity WHERE id = %s"""
			result = self.bdd.delete(query, (id,))
			if result:
				return "La donnée a bien été supprimée de la BDD."
			else:
				return "La donnée n'a pas été supprimée de la BDD."
		except:
			return "[Entity-Delete] - Error"