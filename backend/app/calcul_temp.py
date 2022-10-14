import numpy
from scipy.integrate import odeint

def calcul_scipy_temp(minutes: int, temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float):
	time = numpy.linspace(0, 30)
	y = odeint(func=calcul_scipy, y0=temperature_cable, t=time, args=(temperature_ambiant,intensity, wind_speed))
	return y

def calcul_scipy(y, t, temperature_ambiant: float, intensity: int, wind_speed: float):
	# Repris de calcul_temp, devrait calculer la température
	# Mais n'ayant pas utilisé scipy auparavant, je ne sais pas trop ...
	part1 = ((wind_speed * wind_speed) / 1600) * 0.4 - 0.1
	part2 = (y - temperature_ambiant - ((pow(intensity, 1.4) / 73785) * 130))
	temperature_total = part1 * part2
	return temperature_total

def calcul_temp_minutes(minutes: int, temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float):
	# calcul sur les 30 prochaines minutes
	for minute in range(minutes):
		temperature_cable = calcul_temp_minute(temperature_cable, temperature_ambiant, intensity, wind_speed)
		# print({'time': minute, 'temp': temperature_cable}, flush=True)
	return temperature_cable

def calcul_temp_minute(temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float):
	# Retourne la température du cable dans une simulation de 1 minute aux paramètres donnés
	for time in range(1, 60):
		temperature_cable += calcul_temp(temperature_cable, temperature_ambiant, intensity, wind_speed)
	return temperature_cable

def calcul_temp(temperature_cable: float, temperature_ambiant: float, intensity: int, wind_speed: float) -> float:
	# Retourne le calcul de la température
	# formule de chauffe du cable toutes les secondes selon les paramètres donnés
	# temperature_cable doit etre la temperature de la dernière itération de la formule
	# wind speed en m/s
	part1 = ((wind_speed * wind_speed) / 1600) * 0.4 - 0.1
	part2 = (temperature_cable - temperature_ambiant - ((pow(intensity, 1.4) / 73785) * 130))
	temperature_total = part1 * part2
	return temperature_total
