#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Appareil:

	capacite = 0
	duree_de_vie=0
	delai_de_reaction=0
	rendement = 0
	puissance = 0
	stock = 0

	def __init__(self, id):
		self.id = _id

	#On stock le max sans depasser la capacite
	def stocker(self, v):
		stock = min(stock + v, capacite)

	#on destocke le plus possible et on indique si on a assez pour tout
	def destocker(self, v):
		if stock > v :
			stock = stock - v
			return (True,0)
		else :
			return (False,v-stock)


if __name__=='__main__':
	print("tourne")