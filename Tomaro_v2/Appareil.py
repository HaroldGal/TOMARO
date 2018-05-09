#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Appareil:

	def __init__(self, nom , consommation_watt_heure):

		# Nom de l'appareil
		self.nom = nom

		# Attribut pour savoir si l'appareil est allumé ou non
		self.allume = False

		# Consommation
		self.consommation_heure = consommation_watt_heure
		self.consommation_minute = consommation_watt_heure/60



class Electro(Appareil):

	def __init__(self, nom , consommation_watt_heure):

		Appareil.__init__(self, nom, consommation_watt_heure)

		#Nombre de fois que l'appareil a été allumé (utile pour les chevauchements d'allumage)
		self.nb_allumage = 0

class Frigo(Appareil):

	def __init__(self, nom , consommation_watt_heure):

		Appareil.__init__(self, nom, consommation_watt_heure)

		#Temperature interne du frigo en °C
		self.temperature = 3.0
		self.volume = 1.0
		self.surface = 3.0
		self.lamb = 0.02
		self.epaisseur = 0.02
