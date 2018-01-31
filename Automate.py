#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Automate:

<<<<<<< HEAD
	def __init__(self):
		return

	def tic(self, liste_production, liste_stockage, liste_appareil):
		production_globale = 0
		
		if consommation_globale() < production_globale():
			surplus = production_globale - consommation_globale()
=======
	def __init__(self, _liste_production, _liste_stockage, _liste_appareil):
		self.liste_production = _liste_production
		self.liste_appareil = _liste_appareil
		self.liste_stockage = liste_stockage
		self.energie_totale_manquante = 0
		return

	def gestion_du_stockage():
		production_globale, consommation_globale = 0, 0

		for appareil in liste_appareil:
			consommation_globale += appareil.conso()

		for moyen_production in liste_production:
			production_globale = moyen_production.production()

		########## On produit plus que l'on consomme ##########
		if consommation_globale < production_globale:
			surplus = production_globale - consommation_globale
>>>>>>> ed1dffc68370ca251469151bbbad2edfe60ca672

			for moyen_stockage in liste_stockage:
				surplus = moyen_stockage.stocker(surplus)
				if surplus == 0:
					break
<<<<<<< HEAD

		elif consommation_globale() > production_globale():
			manque = consommation_globale() - production_globale()
=======
		########## On produit moins que l'on consomme ##########
		elif consommation_globale > production_globale:
			manque = consommation_globale - production_globale
>>>>>>> ed1dffc68370ca251469151bbbad2edfe60ca672
			for moyen_stockage in liste_stockage:
				manque = moyen_stockage.destocker(manque)
				if manque == 0:
					break
			if manque !=0 :
<<<<<<< HEAD
				#acheter de lenergie a EDF
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
=======
				self.energie_totale_manquante += manque # il faudra acheter tant denergie a EDF
>>>>>>> ed1dffc68370ca251469151bbbad2edfe60ca672


if __name__=='__main__':
	print("Compilation OK")
