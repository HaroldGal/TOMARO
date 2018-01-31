#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class MoyenProduction:

	def __init__(self, _nom, position):
		self.nom = _nom
		self.energie=0
		self.position = position
		self.allume = True

	def energie(self):
		return energie

	def eteindre():
		self.allume = False

	def allumer():
		self.allume = True



class Eolienne(MoyenProduction):
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+1

class PanneauPhotovoltaique(MoyenProduction):
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+2

if __name__=='__main__':
	p=Eolienne(1)
	for i in range(5):
		p.production()

	print(p.energie)
