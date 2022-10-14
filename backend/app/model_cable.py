# Fichier - Classe - Vent

class Cable:

    # méthode qui s'exécutera la première fois que nous créerons un nouveau résultat 
	def __init__(self, heure, temperature_cable, temperature_ambiant, intensity, wind_speed):
		self.heure = heure
		self.temperature_cable = temperature_cable
		self.temperature_ambiant = temperature_ambiant
		self.intensity = intensity
		self.wind_speed = wind_speed

	# méthode pour représenter l'objet lorsque nous l'interrogerons
	def __repr__(self):
		return '<id {}>'.format(self.id)