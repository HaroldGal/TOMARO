#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from Appareil import *
from random import randrange

class Personne:

	def __init__(self,liste_image_personne_deja_presente):
		#Attribut un nom d'image aléatoire
		nom_image="Image/Personnage/Perso_"+str(randrange(1,16))+".png"
		while(nom_image in liste_image_personne_deja_presente): 
			nom_image="Image/Personnage/Perso_"+str(randrange(1,16))+".png"
		self.image=nom_image
		
		# Initialisation de la télé 
		self.tv = Appareil("TV",100+randrange(-10,10)) #+ ou - 10%
		self.tv_h_jt = dict() # dictionnaire de l'utilisation de la télé par une personne lors des jours travaillés [plage:temps]
		self.tv_h_jnt = dict() # dictionnaire de l'utilisation de la télé par une personne lors des jours non travaillés [plage:temps]
		self.allumage_tv_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_tv_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation de l'ordinateur
		self.pc = Appareil("PC",80+randrange(-16,16)) #+ ou - 20%
		self.pc_h_jt = dict() # dictionnaire de l'utilisation de l'ordinateur par une personne lors des jours travaillés [plage:temps]
		self.pc_h_jnt = dict() # dictionnaire de l'utilisation de l'ordinateur par une personne lors des jours non travaillés [plage:temps]
		self.allumage_pc_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_pc_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation des plaques à inductions (pai) 
		self.pai = Appareil("PAI",9000+randrange(-900,900)) #+ ou - 10%
		self.pai_h_jt = dict() # dictionnaire de l'utilisation des plaques à inductions par une personne lors des jours travaillés [plage:temps]
		self.pai_h_jnt = dict() # dictionnaire de l'utilisation des plaques à inductions par une personne lors des jours non travaillés [plage:temps]
		self.allumage_pai_h = -1 # heure d'allumage recalculer à chaque nouvelle plage
		self.eteignage_pai_h = -1 # heure d'eteignage recalculer à chaque nouvelle plage

		# Initialisation des Appareils électroménagé
		self.electro = Electro("ELECTRO",1000+randrange(-250,250)) #+ ou - 25%
		self.electro_h_jt = dict() # dictionnaire de l'utilisation des Appareils électroménagés par une personne lors des jours travaillés [plage:nb_fois_utilisé]
		self.electro_h_jnt = dict() # dictionnaire de l'utilisation des Appareils électroménagés par une personne lors des jours non travaillés [plage:nb_fois_utilisé]
		self.liste_allumage_h = [] # horaire d'allumage des Appareils recalculer à chaque nouvelle plage
		self.liste_eteignage_h = [] # horaire d'eteignage des Appareils recalculer à chaque nouvelle plage
		
		#Initialisation de la lampe de la personne
		self.lampe = Appareil("LAMPE",60+randrange(-6,6)) #+ ou - 10%

		# Initialisation du nombre de machine dans la semaine
		self.machine_a_laver = -1
		self.lave_vaisselle = -1
		self.seche_linge = -1

		# Initialisaiton de climatisation et chauffage d'appoint
		self.climatisation = False
		self.chauffage = False

	def afficher(self):
		print "\n",self.tv.nom,"jours travaillés:",self.tv_h_jt,"jours non travaillés:",self.tv_h_jnt
		print "\n",self.pc.nom,"jours travaillés:",self.pc_h_jt,"jours non travaillés:",self.pc_h_jnt
		print "\n",self.pai.nom,"jours travaillés:",self.pai_h_jt,"jours non travaillés:",self.pai_h_jnt
		print "\n",self.electro.nom,"jours travaillés:",self.electro_h_jt,"jours non travaillés:",self.electro_h_jnt
		print "\nMachine à laver:",self.machine_a_laver,"Lave-vaisselle:",self.lave_vaisselle,"Seche-linge:",self.seche_linge
		print "\nClimatisation:",self.climatisation,"Chauffage:",self.chauffage
