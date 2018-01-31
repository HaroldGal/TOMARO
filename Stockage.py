#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class MoyenStockage:

	capacite = 0
	#delai_de_reaction=0
	rendement = 0
	puissance = 0
	stock = 0

	def __init__(self, _id, capa, _rend, _p):
		self.id = _id
		self.capacite = capa
		#delai_de_reaction=0
		self.rendement = _rend
		self.puissance = _p
		stock = 0

	#On stock le max sans depasser la capacite
	def stocker(self, v):
		if capacite > stock + v
			stock = stock +v
			return 0  #Il ne reste rien a stocker
		else :
			stock = capacite
			return v - (capacite-stock) # combien il reste denergie a stocker

	#on destocke le plus possible et on indique si on a assez pour tout
	def destocker(self, v):
		if stock > v :
			stock = stock - v
			return 0
		else :
			return v-stock


if __name__=='__main__':
	print("tourne")