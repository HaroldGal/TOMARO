#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

LienSondage = "Data/SondageHabitudes.csv"
import csv
from random import sample, seed
from Personne import *
from math import sqrt

class Foyer:

	def __init__(self, nombre_individu):

		self.temperature = 10.0
		self.liste_personne = []

		self.climatisation_presente = True
		self.chauffage = True
		self.frigo = Frigo("Frigo",175+randrange(-25,25))
		self.frigo.allume=True

		self.nb_machine_a_laver = 0
		self.machine_a_laver = Appareil("Machine_a_laver",470+randrange(-47,47))
		self.heure_jour_on_off_machine_a_laver = dict() #Dictionnaire permettant de stocker l'heure d'allumage de la machine

		self.nb_lave_vaisselle = 0
		self.lave_vaisselle = Appareil("Lave_vaisselle",500+randrange(-50,50))
		self.heure_jour_on_off_lave_vaisselle = dict() #Dictionnaire permettant de stocker l'heure d'allumage de la machine

		self.nb_seche_linge = 0
		self.seche_linge = Appareil("Seche_linge",1700+randrange(-170,170))
		self.heure_jour_on_off_seche_linge = dict() #Dictionnaire permettant de stocker l'heure d'allumage de la machine
		self.radiateur=Appareil("Radiateur 1",750+randrange(-50,50))

		self.climatisation=Appareil("climatisation",750+randrange(-50,50))

		self.nombre_individu = nombre_individu
		self.ajouter_individu()
		self.habitude_foyer()
		self.surface_mur = sqrt(25*nombre_individu)*4*2.5
		self.epaisseur_mur = 0.20
		self.volume = 25*nombre_individu*2.5
		self.coef_isolation=1.5

	def habitude_foyer(self):
		cpt_climatisation = 0
		cpt_chauffage = 0

		for individu in self.liste_personne:
			self.nb_machine_a_laver = individu.machine_a_laver if (self.nb_machine_a_laver<individu.machine_a_laver) else self.nb_machine_a_laver
			self.nb_lave_vaisselle = individu.lave_vaisselle if (self.nb_lave_vaisselle<individu.lave_vaisselle) else self.nb_lave_vaisselle
			self.nb_seche_linge = individu.seche_linge if (self.nb_seche_linge<individu.seche_linge) else self.nb_seche_linge
			if(individu.climatisation):
				cpt_climatisation+=1
			if(individu.chauffage):
				cpt_chauffage+=1

		if(float(cpt_climatisation)/float(self.nombre_individu) > 0.5):	
			climatisation = True
		if(float(cpt_chauffage)/float(self.nombre_individu) > 0.5):
			chauffage = True


	def choix_population(self):
		with open(LienSondage, 'rb') as FichierCsv:
			lignes = csv.reader(FichierCsv, delimiter=',')
			choix = sample(range(1,284),self.nombre_individu) # taille de la population on decale de 1 pouur header du csv
			PopulationFoyer = []
			for i, line in enumerate(lignes):
				if i in choix :
					PopulationFoyer.append(line[1:-1])

		return PopulationFoyer

	def ajouter_individu(self):
		#Permet de ne pas avoir deux fois la meme image de personne dans le foyer
		liste_image_personne_deja_presente=[]		

		PopulationDisponible = self.choix_population()
		# print(PopulationDisponible)
		for ligne in PopulationDisponible:
			nouvel_individu = Personne(liste_image_personne_deja_presente)

			# Television jours travaillés
			for index, var in enumerate(ligne[0:7]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.tv_h_jt[0]=int(var)
					else:
						nouvel_individu.tv_h_jt[360 + (index)*180]=int(var)

			# Ordinateurs jours travaillés
			for index, var in enumerate(ligne[7:14]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pc_h_jt[0]=int(var)
					else:
						nouvel_individu.pc_h_jt[360 + (index)*180]=int(var)

			# Plaques à induction jours travaillés
			for index, var in enumerate(ligne[14:21]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pai_h_jt[0]=int(var)
					else:
						nouvel_individu.pai_h_jt[360 + (index)*180]=int(var)

			# Electro ménagers jours travaillés
			for index, var in enumerate(ligne[21:28]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jt[0]=int(var)
					else:
						nouvel_individu.electro_h_jt[360 + (index)*180]=int(var)

			# Electro salle de bain jours travaillés
			for index, var in enumerate(ligne[28:35]):
				if int(var)!=0:
					if index==6:
						if 0 in nouvel_individu.electro_h_jt :
							nouvel_individu.electro_h_jt[0]=nouvel_individu.electro_h_jt[0] + int(var)
						else:
							nouvel_individu.electro_h_jt[0]=int(var)
					else:
						if 360 + (index)*180 in nouvel_individu.electro_h_jt :
							nouvel_individu.electro_h_jt[360 + (index)*180]=nouvel_individu.electro_h_jt[360 + (index)*180] + int(var)
						else:
							nouvel_individu.electro_h_jt[360 + (index)*180]=int(var)

			# Television jours non travaillés
			for index, var in enumerate(ligne[35:42]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.tv_h_jnt[0]=int(var)
					else:
						nouvel_individu.tv_h_jnt[360 + (index)*180]=int(var)

			# Ordinateurs jours non travaillés
			for index, var in enumerate(ligne[42:49]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pc_h_jnt[0]=int(var)
					else:
						nouvel_individu.pc_h_jnt[360 + (index)*180]=int(var)

			# Plaques à induction jours non travaillés
			for index, var in enumerate(ligne[49:56]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pai_h_jnt[0]=int(var)
					else:
						nouvel_individu.pai_h_jnt[360 + (index)*180]=int(var)

			# Electro ménager jours non travaillés
			for index, var in enumerate(ligne[56:63]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jnt[0]=int(var)
					else:
						nouvel_individu.electro_h_jnt[360 + (index)*180]=int(var)

			# Electro salle de bain jours non travaillés
			for index, var in enumerate(ligne[63:70]):
				if int(var)!=0:
					if index==6:
						if 0 in nouvel_individu.electro_h_jnt :
							nouvel_individu.electro_h_jnt[0]=nouvel_individu.electro_h_jnt[0] + int(var)
						else:
							nouvel_individu.electro_h_jnt[0]=int(var)
					else:
						if 360 + (index)*180 in nouvel_individu.electro_h_jnt :
							nouvel_individu.electro_h_jnt[360 + (index)*180]=nouvel_individu.electro_h_jnt[360 + (index)*180] + int(var)
						else:
							nouvel_individu.electro_h_jnt[360 + (index)*180]=int(var)

			nouvel_individu.machine_a_laver = int(ligne[70])
			nouvel_individu.lave_vaisselle = int(ligne[71])
			nouvel_individu.seche_linge = int(ligne[72])

			if(ligne[73]=="Oui"):
				nouvel_individu.climatisation = True

			if(ligne[74]=="Oui"):
				nouvel_individu.chauffage = True

			self.liste_personne.append(nouvel_individu)
			liste_image_personne_deja_presente.append(nouvel_individu.image)


if __name__=='__main__':
	seed(3)
	a = Foyer(1)
	for i in a.liste_personne :
		i.afficher()
	#a.CsvParse()