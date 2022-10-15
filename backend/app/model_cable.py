# Fichier - Classe - Vent

from app.calcul_temp import calcul_temp, calcul_temp_minutes

class Cable:

	# Constructeur
	def __init__(self, heure, temperature_cable, temperature_ambiant, intensity, wind_speed):
		self.heure = heure
		self.temperature_cable = temperature_cable
		self.temperature_ambiant = temperature_ambiant
		self.intensity = intensity
		self.wind_speed = wind_speed
	
	def calcul(self):
		return calcul_temp(self.temperature_cable, self.temperature_ambiant, self.intensity, self.wind_speed)
		
	def calcul_minutes(self, minutes: int):
		return calcul_temp_minutes(minutes, self.temperature_cable, self.temperature_ambiant, self.intensity, self.wind_speed)

	# ToString
	def __repr__(self):
		return '<cable {}>'.format(self.__class__)