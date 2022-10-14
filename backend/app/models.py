# Fichier Models
from backend.app import db


# Entité - Vent
class Vent(db.Model):
    # table name
    __tablename__ = 'vent'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    heure = db.Column(db.DateTime, nullable=True)
    intencite = db.Column(db.Float, nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    vitesse = db.Column(db.Float, nullable=True)

    # méthode qui s'exécutera la première fois que nous créerons un nouveau résultat 
    def __init__(self, heure, intencite, temperature, vitesse):
        self.heure = heure
        self.intencite = intencite
        self.temperature = temperature
        self.vitesse = vitesse

    # méthode pour représenter l'objet lorsque nous l'interrogerons
    def __repr__(self):
        return '<id {}>'.format(self.id)
