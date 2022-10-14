# Fichier - Controlle - Entity
from app import db
from model_entity import Entity

# Entité - Vent
class ControllerEntity:

    self.bdd = None
    
    def __init__(self, bdd):
        super().__init__()
        self.bdd = bdd

    def all(self):
        try:
            query = """SELECT * FROM entity"""
            result = self.bdd.getAll(query)
            if len(result)>0:
                return [ { result } ]
            else:
                return "Il n'y a pas de données dans la BDD."
        except:
            return "[Entity-Create] - Error"