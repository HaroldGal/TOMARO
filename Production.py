#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Production:

	def __init__(self, _nom):
		self.nom = _nom
		self.energie=50
		self.allume = True

	def energie(self):
		return energie

	def eteindre():
		self.allume = False

	def allumer():
		self.allume = True



class Eolienne(Production):
	
	def __init__(self, identite):
		self.id = identite

	def production(self):
		self.energie= self.energie+1

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
		self.energie=float(self.rendement)*float(self.radiation)*float(self.surface)
		return(self.energie)

if __name__=='__main__':
	p=Eolienne(1)
	for i in range(5):
		p.production()

	print(p.energie)
