#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

LienSondage = "Data/SondageHabitudes.csv"
import csv
from random import sample
from Personne import Personne


class Foyer:

	Individus = []

	def __init__(self, _nombreIndividu):
		self.nombreIndividu = _nombreIndividu
		self.ajouterIndividus()

	def ChoixPopulation(self, lien):
		with open(lien, 'rb') as FichierCsv:
			lignes = csv.reader(FichierCsv, delimiter=',')
			choix = [ x+1 for x in sample(range(283),self.nombreIndividu)] # taille de la population on decale de 1 pouur header du csv
			PopulationFoyer = []
			for i, line in enumerate(lignes):
				if i in choix :
					PopulationFoyer.append(line[1:-1])
					print i

		return PopulationFoyer

	def ajouterIndividus(self):
		PopulationDisponible = self.ChoixPopulation(LienSondage)
		# print(PopulationDisponible)
		for ligne in PopulationDisponible:
			nouvelIndividu = Personne()

			for index, var in enumerate(ligne[0:7]):
				if int(var)!=0:
					if index==0:
						nouvelIndividu.tv_h_jt[0]=int(var)
					else:
						nouvelIndividu.tv_h_jt[360+(index-1)*180]=int(var)
			print nouvelIndividu.tv_h_jt

			print "VÉRIFIER QUE LES VALEURS SONT BON!!!!!!!!!!!!!!!!!!"
			print "VÉRIFIER QUE LES VALEURS SONT BON!!!!!!!!!!!!!!!!!!"
			print "VÉRIFIER QUE LES VALEURS SONT BON!!!!!!!!!!!!!!!!!!"
			print "VÉRIFIER QUE LES VALEURS SONT BON!!!!!!!!!!!!!!!!!!"

			# nouvelIndividu.tv_h_jt=
			# nouvelIndividu.tv_h_jnt=
			# nouvelIndividu.pc_h_jt=


			# Individus.append(Personne())	


if __name__=='__main__':
	a = Foyer(5)
	#a.CsvParse()