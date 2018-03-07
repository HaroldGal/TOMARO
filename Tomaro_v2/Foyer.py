#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

LienSondage = "Data/SondageHabitudes.csv"
import csv
from random import sample, seed
from Personne import Personne


class Foyer:

	liste_personne = []

	def __init__(self, _nombreIndividu):
		self.nombre_individu = _nombreIndividu
		self.ajouterIndividus()

	def ChoixPopulation(self):
		with open(LienSondage, 'rb') as FichierCsv:
			lignes = csv.reader(FichierCsv, delimiter=',')
			choix = sample(range(1,284),self.nombre_individu) # taille de la population on decale de 1 pouur header du csv
			PopulationFoyer = []
			for i, line in enumerate(lignes):
				if i in choix :
					PopulationFoyer.append(line[1:-1])

		return PopulationFoyer

	def ajouterIndividus(self):
		PopulationDisponible = self.ChoixPopulation()
		# print(PopulationDisponible)
		for ligne in PopulationDisponible:
			nouvel_individu = Personne()

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


			for index, var in enumerate(ligne[14:21]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pai_h_jt[0]=int(var)
					else:
						nouvel_individu.pai_h_jt[360 + (index)*180]=int(var)

			for index, var in enumerate(ligne[21:28]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jt[0]=int(var)
					else:
						nouvel_individu.electro_h_jt[360 + (index)*180]=int(var)

			for index, var in enumerate(ligne[28:35]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jt[0]=nouvel_individu.electro_h_jt[0] + int(var)
					else:
						nouvel_individu.electro_h_jt[360 + (index)*180]=nouvel_individu.electro_h_jt[360 + (index)*180] + int(var)

			for index, var in enumerate(ligne[35:42]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.tv_h_jnt[0]=int(var)
					else:
						nouvel_individu.tv_h_jnt[360 + (index)*180]=int(var)

			# Ordinateurs jours travaillés
			for index, var in enumerate(ligne[42:49]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pc_h_jnt[0]=int(var)
					else:
						nouvel_individu.pc_h_jnt[360 + (index)*180]=int(var)


			for index, var in enumerate(ligne[49:56]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.pai_h_jnt[0]=int(var)
					else:
						nouvel_individu.pai_h_jnt[360 + (index)*180]=int(var)

			for index, var in enumerate(ligne[56:63]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jnt[0]=int(var)
					else:
						nouvel_individu.electro_h_jnt[360 + (index)*180]=int(var)

			for index, var in enumerate(ligne[63:70]):
				if int(var)!=0:
					if index==6:
						nouvel_individu.electro_h_jnt[0]=nouvel_individu.electro_h_jt[0] + int(var)
					else:
						nouvel_individu.electro_h_jnt[360 + (index)*180]=nouvel_individu.electro_h_jt[360 + (index)*180] + int(var)

			nouvel_individu.machine_a_laver = int(ligne[70])
			nouvel_individu.lave_vaisselle = int(ligne[71])
			nouvel_individu.seche_linge = int(ligne[72])

			if(ligne[73]=="Oui"):
				nouvel_individu.climatisation = True

			if(ligne[74]=="Oui"):
				nouvel_individu.chauffage = True

			self.liste_personne.append(nouvel_individu)	


if __name__=='__main__':
	seed(3)
	a = Foyer(5)
	#a.CsvParse()