# Fichier Models
from backend.app import bdd


# Entité - Vent
class Vent(bdd.Model):
    # table name
    __tablename__ = 'vent'

    # columns
    id = bdd.Column(bdd.Integer, primary_key=True)
    heure = bdd.Column(bdd.DateTime, nullable=True)
    intencite = bdd.Column(bdd.Float, nullable=True)
    temperature = bdd.Column(bdd.Float, nullable=True)
    vitesse = bdd.Column(bdd.Float, nullable=True)

    # méthode qui s'exécutera la première fois que nous créerons un nouveau résultat 
    def __init__(self, heure, intencite, temperature, vitesse):
        self.heure = heure
        self.intencite = intencite
        self.temperature = temperature
        self.vitesse = vitesse

    # méthode pour représenter l'objet lorsque nous l'interrogerons
    def __repr__(self):
        return '<id {}>'.format(self.id)
