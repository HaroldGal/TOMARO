#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from Foyer import *
from random import randrange,sample

class Site:

	def __init__(self, nom, nb_foyer):

		self.nom = nom
		self.nb_foyer = nb_foyer
		self.consommation_globale_minute = 0	

		#Initialisation de la liste des foyers
		self.liste_foyer = self.init_liste_foyer(nb_foyer)

		#Initialisaiton de la liste des productions
		self.liste_production = self.init_liste_production()

		#Initialisation de la liste des stockages
		self.liste_stockage = self.init_liste_stockage()

		#Nombre d'habitant du site
		self.nb_personne = self.compteur_personne()
		
	#Fonction permettant de renvoyer la liste avec tous les foyers du site
	def init_liste_foyer(self, nb_foyer):

		liste_foyer = []
		#Chaque foyer à 4 personnes max
		for i in range(0,nb_foyer):
			liste_foyer.append(Foyer(randrange(1,4)))

		return liste_foyer

	#Fonction permettant de renvoyer la liste avec tous les productions du site
	def init_liste_production(self):
		#lecture du fichier
		print "Liste production pas encore codé"
		return []

	#Fonction permettant de renvoyer la liste avec tous les stockages du site
	def init_liste_stockage(self):
		#lecture du fichier
		print "Liste stockage pas encore codé"
		return []

	#Renvoie le nombre d'habitant du site
	def compteur_personne(self):

		nb_personne = 0
		for foyer in self.liste_foyer:
			nb_personne = nb_personne + len(foyer.liste_personne)			

		return nb_personne

	#Modifie les heures d'allumage et d'éteignage des appareils
	def actualisation_des_plages_h(self,minute,jour):		

		#Si on est entre lundi et vendredi et qu'on est sur une plage de mofication on calcul l'heure d'allumage et d'éteignage
		if(jour<5):
			for foyer in self.liste_foyer:
				for personne in foyer.liste_personne:
					#Gestion TV
					#Si la plage est dans la liste
					if(minute in personne.tv_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_tv_h = minute + randrange(0,361-personne.tv_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_tv_h = minute + randrange(0,181-personne.tv_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_tv_h = personne.allumage_tv_h + personne.tv_h_jt[minute] 

					if(minute in personne.pc_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pc_h = minute + randrange(0,361-personne.pc_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pc_h = minute + randrange(0,181-personne.pc_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pc_h = personne.allumage_pc_h + personne.pc_h_jt[minute]

					if(minute in personne.pai_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pai_h = minute + randrange(0,361-personne.pai_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pai_h = minute + randrange(0,181-personne.pai_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pai_h = personne.allumage_pai_h + personne.pai_h_jt[minute]

					if(minute in personne.electro_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.liste_allumage_h = sample(range(0,355),personne.electro_h_jt[minute]) 
						else:
							personne.liste_allumage_h = sample(range(0,175),personne.electro_h_jt[minute])

						personne.liste_eteignage_h = [temps+5 for temps in personne.liste_allumage_h]

		#Si on est samedi ou dimanche et qu'on est sur une plage de mofication on calcul l'heure d'allumage et d'éteignage
		elif(jour>=5):
			for foyer in self.liste_foyer:
				for personne in foyer.liste_personne:
					#Gestion TV
					#Si la plage est dans la liste
					if(minute in personne.tv_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_tv_h = minute + randrange(0,361-personne.tv_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_tv_h = minute + randrange(0,181-personne.tv_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_tv_h = personne.allumage_tv_h + personne.tv_h_jnt[minute] 

					if(minute in personne.pc_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pc_h = minute + randrange(0,361-personne.pc_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pc_h = minute + randrange(0,181-personne.pc_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pc_h = personne.allumage_pc_h + personne.pc_h_jnt[minute]

					if(minute in personne.pai_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pai_h = minute + randrange(0,361-personne.pai_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pai_h = minute + randrange(0,181-personne.pai_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pai_h = personne.allumage_pai_h + personne.pai_h_jnt[minute]

					if(minute in personne.electro_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.liste_allumage_h = sample(range(0,355),personne.electro_h_jnt[minute]) 
						else:
							personne.liste_allumage_h = sample(range(0,175),personne.electro_h_jnt[minute])

						personne.liste_eteignage_h = [temps+5 for temps in personne.liste_allumage_h]
						
	#Allume ou éteint les appareils en fonction de l'heure de la journée
	def actualisation_des_foyers(self,minute):

		self.consommation_globale_minute = 0

		for foyer in self.liste_foyer:
				for personne in foyer.liste_personne:

					#--------------- On regarde si on doit allumer ou éteindre les appareils ---------------#
					if(personne.allumage_tv_h == minute):
						personne.tv.allume = True
					elif(personne.eteignage_tv_h == minute):
						personne.tv.allume = False

					if(personne.allumage_pc_h == minute):
						personne.pc.allume = True
					elif(personne.eteignage_pc_h == minute):
						personne.pc.allume = False

					if(personne.allumage_pai_h == minute):
						personne.pai.allume = True
					elif(personne.eteignage_pai_h == minute):
						personne.pai.allume = False

					for minute_allumage in personne.liste_allumage_h:
						if(minute_allumage == minute):
							personne.electro.allume = True
							personne.electro.nb_allumage = personne.electro.nb_allumage + 1

					for minute_eteignage in personne.liste_eteignage_h:
						if(minute_eteignage == minute):							
							personne.electro.nb_allumage = personne.electro.nb_allumage - 1
							if(personne.electro.nb_allumage == 0):
								personne.electro.allume = False

					#--------------- Calcule de la consommation globale ---------------#
					if(personne.tv.allume == True):
						self.consommation_globale = self.consommation_globale_minute + personne.tv.consommation_minute
					if(personne.pc.allume == True):
						self.consommation_globale_minute = self.consommation_globale_minute + personne.pc.consommation_minute
					if(personne.pai.allume == True):
						self.consommation_globale_minute = self.consommation_globale_minute + personne.pai.consommation_minute
					if(personne.electro.allume == True):
						self.consommation_globale_minute = self.consommation_globale + personne.electro.consommation_minute*personne.electro.nb_allumage