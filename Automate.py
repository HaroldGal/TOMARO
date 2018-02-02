#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Automate:

	def __init__(self):
		#Permet de connaitre l'énergie manquante à la fin
		self.energie_totale_manquante = 0
		#Permet de connaitre le nombre de fois qu'à fonctionné l'automate (en seconde)
		self.tic_total=0
		#Permet de savoir combien de fois on a manqué d'énergie
		self.tic_energie_manquante=0
		return

	def gestion_du_stockage(self,liste_production, liste_stockage, liste_appareil,affichage,longueur_fenetre,hauteur_fenetre):
		conso = self.consommation_globale(liste_appareil)
		prod = self.production_globale(liste_production)
		self.tic_total+=1

		#On reset les traits
		for index2,moyen_stockage in enumerate(liste_stockage):				
			affichage.connexion_stockage(index2,longueur_fenetre,hauteur_fenetre,"Reset")

		########## On produit plus que l'on consomme ##########
		if conso < prod:
			surplus = prod - conso

			for index1,moyen_stockage in enumerate(liste_stockage):
				surplus = moyen_stockage.stocker(surplus)

				#On reset les traits
				for index2,moyen_stockage in enumerate(liste_stockage):
					affichage.connexion_stockage(index2,longueur_fenetre,hauteur_fenetre,"Reset")			

				#Si le stockage est pas plein (pour pas freeze dessus)
				if moyen_stockage.stockage!=moyen_stockage.capacite:
					#Si on stock on affiche le trait correspondant
					affichage.connexion_stockage(index1,longueur_fenetre,hauteur_fenetre,"Green")					

				if surplus == 0:
					break			

			return "surplus"
		
		########## On produit moins que l'on consomme ##########
		elif conso > prod:
			manque = conso - prod
			for index1,moyen_stockage in enumerate(liste_stockage):
				manque = moyen_stockage.destocker(manque)

				#On reset les traits
				for index2,moyen_stockage in enumerate(liste_stockage):
					affichage.connexion_stockage(index2,longueur_fenetre,hauteur_fenetre,"Reset")

				if moyen_stockage.stockage!=0:
					#Si on stock on affiche le trait correspondant
					affichage.connexion_stockage(index1,longueur_fenetre,hauteur_fenetre,"Green")
				

				if manque == 0:
					break
			if manque !=0 :
				self.energie_totale_manquante += manque # il faudra acheter tant denergie a EDF
				self.tic_energie_manquante+=1
				print "Manque d'énergie",str(100-self.tic_energie_manquante*100/self.tic_total)+"%"+" du temps"
				print self.tic_energie_manquante,"/",self.tic_total,"energie manquante:",self.energie_totale_manquante

			return "manque"

		
				
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

	def stockage_global(self,liste_stockage):
		stockage_globale=0
		capacite_globale=0
		for stockage in liste_stockage:
			stockage_globale+=stockage.stockage
			capacite_globale+=stockage.capacite

		return (stockage_globale,capacite_globale)			



if __name__=='__main__':
	print("Compilation OK")
