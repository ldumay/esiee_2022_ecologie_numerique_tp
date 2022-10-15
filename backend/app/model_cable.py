# Fichier - Classe - Vent

class Cable:

	# Constructeur
	def __init__(self, heure, temperature_cable, temperature_ambiant, intensity, wind_speed):
		self.heure = heure
		self.temperature_cable = temperature_cable
		self.temperature_ambiant = temperature_ambiant
		self.intensity = intensity
		self.wind_speed = wind_speed

	# ToString
	def __repr__(self):
		return '<id {}>'.format(self.id)