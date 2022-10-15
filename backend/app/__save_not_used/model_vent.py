# Fichier - Classe - Vent
from app import db

# Classe - Vent
class Vent:

    # méthode qui s'exécutera la première fois que nous créerons un nouveau résultat 
    def __init__(self, heure, intencite, temperature, vitesse):
        self.heure = heure
        self.intencite = intencite
        self.temperature = temperature
        self.vitesse = vitesse

    # méthode pour représenter l'objet lorsque nous l'interrogerons
    def __repr__(self):
        return '<id {}>'.format(self.id)