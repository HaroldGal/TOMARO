#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Automate:

	def __init__(self):
		self.energie_totale_manquante = 0
		return

	def gestion_du_stockage(liste_production, liste_stockage, liste_appareil):
		conso = consommation_globale(liste_appareil)
		prod = production_globale(liste_production)
		########## On produit plus que l'on consomme ##########
		if conso < prod:
			surplus = prod - conso

			for moyen_stockage in liste_stockage:
				surplus = moyen_stockage.stocker(surplus)
				if surplus == 0:
					break
		
		########## On produit moins que l'on consomme ##########
		elif conso > prod:
			manque = conso - prod
			for moyen_stockage in liste_stockage:
				manque = moyen_stockage.destocker(manque)
				if manque == 0:
					break
			if manque !=0 :
				self.energie_totale_manquante += manque # il faudra acheter tant denergie a EDF
				print("Manque d'énergie !")
				
		return

	def consommation_globale(self,liste_appareil):
		consommation_globale=0
		for appareil in liste_appareil:
			consommation_globale += appareil.conso

		return consommation_globale

	def production_globale(self,liste_production):
		production_globale=0
		for production in liste_production:
			production_globale += production.energie

		return production_globale
				



if __name__=='__main__':
	print("Compilation OK")
