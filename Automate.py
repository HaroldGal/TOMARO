#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Automate:

	def __init__(self, _liste_production, _liste_stockage, _liste_appareil):
		self.liste_production = _liste_production
		self.liste_appareil = _liste_appareil
		self.liste_stockage = liste_stockage
		time = 0
		return

	def tic():
		production_globale, consommation_globale = 0, 0
		for appareil in liste_appareil:
			consommation_globale += appareil.conso()
		for moyen_production in liste_production:
			production_globale = moyen_production.production

		if consommation_globale < production_globale:
			surplus = production_globale - consommation_globale

			for moyen_stockage in liste_stockage:
				surplus = moyen_stockage.stocker(surplus)
				if surplus == 0:
					break

		elif consommation_globale > production_globale:
			manque = consommation_globale - production_globale
			for moyen_stockage in liste_stockage:
				manque = moyen_stockage.destocker(manque)
				if manque == 0:
					break
			if manque !=0 :
				#acheter de lenergie a EDF
				print("gerer l'achat d'énergie a EDF")
				
		return 

if __name__=='__main__':
	print("cc")