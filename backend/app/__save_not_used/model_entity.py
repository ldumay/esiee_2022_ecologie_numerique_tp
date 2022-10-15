# Fichier - Classe - Entity
from app import db

# Classe - Entité - (exemple de classe utilisant la migration Migrate de Flask)
class Entity(db.Model):
    # table name
    __tablename__ = 'vent'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Float, nullable=True)
    type = db.Column(db.Float, nullable=True)

    # méthode qui s'exécutera la première fois que nous créerons un nouveau résultat 
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

    # méthode pour représenter l'objet lorsque nous l'interrogerons
    def __repr__(self):
        return '<id {}>'.format(self.id)