#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import requests
from pprint import pprint
import math



class Production:

	def __init__(self, _nom):
		self.nom = _nom
		self.energie=50
		self.allume = True

	def energie(self):
		return self.energie

	def eteindre():
		self.allume = False

	def allumer():
		self.allume = True



class Eolienne(Production):
	
	def __init__(self, identite):
		self.id = identite
		self.diametre=10
		self.rendement=0.4

	def production(self):
		r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&lang=fr&type=accurate&appid=ef60c8bbf95eacceaa3001970e3937ed")
		data = r.json()

		self.energie= 0.5*math.pi*(self.diametre/2)**2*data["wind"]["speed"]**3*1.2*self.rendement
		print(self.energie)
		return self.energie

class PanneauPhotovoltaique(Production):
	
	def __init__(self, identite):
		self.id = identite
		self.nom="PanneauPhotovoltaique"
		self.surface = 20.0 # En mètre carré
		self.rendement = 0.14
		self.radiation=0
		

	def set_radiation(self,temps):
		file = open("radiation.txt", "r")
		file.readline()
		for line in file:
			(time,G,Gd,Gc,DNI,DNIc,A,Ad,Ac)=line.split()
			(heure,minute)=time.split(":")
			if temps>=int(heure)*3600+int(minute)*60:
				self.radiation=DNI
		file.close()


	def production(self,temps):
		self.set_radiation(temps)
		self.energie=float(self.rendement)*float(self.radiation)*float(self.surface)/86400
		print(self.energie)
		return(self.energie)

if __name__=='__main__':
	p=PanneauPhotovoltaique(1)
	res = 0
	for i in range(86400):
		res = res + p.production(i)
		print(res)
