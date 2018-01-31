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
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+1

class PanneauPhotovoltaique(Production):
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+2

if __name__=='__main__':
	p=Eolienne(1)
	for i in range(5):
		p.production()

	print(p.energie)
