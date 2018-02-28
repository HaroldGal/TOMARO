#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Personne:

	def __init__(self):
		
		# Initialisation de la télé 
		self.tv = appareil("TV",150)
		self.tv_h_jt = dict() # dictionnaire de l'utilisation de la télé par une personne lors des jours travaillés [plage:temps]
		self.tv_h_jnt = dict() # dictionnaire de l'utilisation de la télé par une personne lors des jours non travaillés [plage:temps]
		self.allumage_tv_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_tv_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation de l'ordinateur
		self.pc = appareil("PC",80)
		self.pc_h_jt = dict() # dictionnaire de l'utilisation de l'ordinateur par une personne lors des jours travaillés [plage:temps]
		self.pc_h_jnt = dict() # dictionnaire de l'utilisation de l'ordinateur par une personne lors des jours non travaillés [plage:temps]
		self.allumage_pc_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_pc_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation des plaques à inductions (pai) 
		self.pai = appareil("PAI",9000)
		self.pai_h_jt = dict() # dictionnaire de l'utilisation des plaques à inductions par une personne lors des jours travaillés [plage:temps]
		self.pai_h_jnt = dict() # dictionnaire de l'utilisation des plaques à inductions par une personne lors des jours non travaillés [plage:temps]
		self.allumage_pai_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_pai_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation des appareils électroménagé
		self.electro = appareil("ELECTRO",1000)
		self.electro_h_jt = dict() # dictionnaire de l'utilisation des appareils électroménagés par une personne lors des jours travaillés [plage:nb_fois_utilisé]
		self.electro_h_jnt = dict() # dictionnaire de l'utilisation des appareils électroménagés par une personne lors des jours non travaillés [plage:nb_fois_utilisé]
		self.liste_allumage_h = [] # horaire d'allumage des appareils recalculer à chaque nouvelle plage
		self.liste_eteignage_h = [] # horaire d'eteignage des appareils recalculer à chaque nouvelle plage
		
		# Initialisation du nombre de machine dans la semaine
		self.machine_a_laver = -1
		self.lave_vaisselle = -1
		self.seche_linge = -1

		# Initialisaiton de climatisation et chauffage d'appoint
		self.climatisation = False
		self.chauffage = False