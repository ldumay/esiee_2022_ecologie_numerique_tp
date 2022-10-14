from backend.app.routes import calcul_temp


class Cable:
    "Definition d'un cable"
    def __init__(self,heure,temperature_cable,temperature_ambiant,intensity,wind_speed):
        self.heure = heure
        self.temperature_cable = temperature_cable
        self.temperature_ambiant = temperature_ambiant
        self.intensity = intensity
        self.wind_speed= wind_speed

    def calcul(self,temperature_cable: int, temperature_ambiant: int, intensity: int, wind_speed: int):
        calcul_temp(self.heure,self.tempext,self.intencite,self.tempint)
