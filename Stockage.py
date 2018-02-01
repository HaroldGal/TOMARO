#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Stockage:

	def __init__(self, _nom, capa, _rend, _p):
		self.nom = _nom
		self.capacite = capa
		#delai_de_reaction=0
		self.rendement = _rend
		self.puissance = _p
		self.stockage = 0

	#On stock le max sans depasser la capacite
	def stocker(self, v):
		if self.capacite > self.stockage + v:
			self.stockage = self.stockage +v
			return 0  #Il ne reste rien a stocker
		else :
			self.stockage = self.capacite
			return v - (self.capacite-self.stockage) # combien il reste denergie a stocker

	#on destocke le plus possible et on indique si on a assez pour tout
	def destocker(self, v):
		if self.stockage > v :
			self.stockage = self.stockage - v
			return 0
		else :
			return v-self.stockage


if __name__=='__main__':
	print("Compilation OK")