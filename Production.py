#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import requests
from pprint import pprint
import math



class Production:

	def __init__(self, _nom):
		self.nom = _nom
		self.puissance=0.0
		self.allume = True


	def energie(self):
		return self.puissance


	def eteindre():
		self.allume = False

	def allumer():
		self.allume = True



class Eolienne(Production):
	
	def __init__(self, identite):
		Production.__init__(self,identite)
		self.id = "EO" #EO pour éolienne
		self.diametre=10.0
		self.rendement=0.4
		self.liste_prod=[]
		file = open("Data/vent_juillet.txt", "r")
		for line in file:
			(temps,vitesse_vent)=line.split()
			(heure,minute)=temps.split(":")
			self.liste_prod.append((int(heure)*3600+int(minute)*60,float(vitesse_vent)))
		file.close()

	def production(self,temps):
		for (horaire,vitesse_vent) in self.liste_prod:
			if temps==horaire:
				self.puissance = round(0.5*math.pi*(self.diametre/2.0)**2*vitesse_vent**3*1.2*self.rendement/60.0,2) # DIVISER PAR 60 POUR AVOIR EN MINUTE
				break
		return self.puissance

	# def production(self):
	# 	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&lang=fr&type=accurate&appid=ef60c8bbf95eacceaa3001970e3937ed")
	# 	data = r.json()

	# 	self.puissance= 0.5*math.pi*(self.diametre/2)**2*data["wind"]["speed"]**3*1.2*self.rendement
	# 	print(self.puissance)
	# 	return self.puissance

class PanneauPhotovoltaique(Production):
	
	def __init__(self, identite):
		Production.__init__(self,identite)
		self.id = identite #PPV panneau photovoltaique 
		self.surface = 20.0 # En mètre carré
		self.rendement = 0.14
		self.radiation=0
		self.liste_prod=[]
		file = open("Data/production_juillet.txt", "r")
		for line in file:
			(temps,production)=line.split()
			(heure,minute)=temps.split(":")
			self.liste_prod.append((int(heure)*3600+int(minute)*60,float(production)))
		file.close()
		


	def production(self,temps):
		for (horaire,production) in self.liste_prod:
			if temps==horaire:
				self.puissance = round(production/60.0,2) # DIVISER PAR 60 POUR AVOIR EN MINUTE
				break
		return self.puissance

	# def set_radiation(self,temps):
	# 	file = open("Data/radiation.txt", "r")
	# 	file.readline()
	# 	for line in file:
	# 		(time,G,Gd,Gc,DNI,DNIc,A,Ad,Ac)=line.split()
	# 		(heure,minute)=time.split(":")
	# 		if temps>=int(heure)*3600+int(minute)*60:
	# 			self.radiation=DNI
	# 	file.close()


	# def production(self,temps):
	# 	self.set_radiation(temps)
	# 	self.puissance=float(self.rendement)*float(self.radiation)*float(self.surface)/86400
	# 	print(self.puissance)
	# 	return(self.puissance)

if __name__=='__main__':
	p=Eolienne(1)
	res = 0.0
	nb_seconde=0.0
	# while True:
	# 	nb_seconde+=60
	# 	nb_seconde=nb_seconde%(24*60*60)
	# 	res = res + p.production(nb_seconde)
	# 	print("La production est de:",p.production(nb_seconde))
	# 	print(res)
	# 	if nb_seconde==0:
	# 		break
	print(p.liste_prod)