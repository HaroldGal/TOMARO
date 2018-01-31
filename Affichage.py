#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import Production
import pygame
import random
import time
from pygame.locals import *

#Classe permettant de gérer l'affichage dans une fenetre
class Affichage:
	
	def __init__(self,longueur_fenetre,hauteur_fenetre):
		#Ouverture de la fenêtre Pygame	
		self.fenetre = pygame.display.set_mode((longueur_fenetre,hauteur_fenetre))
		self.fenetre.fill((60,60,100))
		
	#Méthode permettant d'afficher les modes de production
	def production(self,liste_production,longueur_fenetre,hauteur_fenetre,automate,liste_consommation):

		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_production = pygame.image.load("carre_production.png").convert()

		#On parcourt tous les modes de productions pour les afficher
		for index,production in enumerate(liste_production):
			#Initialisation du texte à écrire
			texte_production=font.render(str(production.energie)+"W : "+str(production.energie*100/automate.consommation_globale(liste_consommation))+"%",1,(0,0,0))
			texte_nom=font.render(production.nom,1,(0,0,0))

			#Affichage en fonction de l'index
			if index < 3:
				self.fenetre.blit(image_production,(50,hauteur_fenetre/2+125*index))
				self.fenetre.blit(texte_production,(100,hauteur_fenetre/2+125*index+50))
				self.fenetre.blit(texte_nom,(100,hauteur_fenetre/2+125*index+20))
			elif index >= 3:
				self.fenetre.blit(image_production,(300,hauteur_fenetre/2+125*(index-3)))
				self.fenetre.blit(texte_production,(350,hauteur_fenetre/2+125*(index-3)+50))
				self.fenetre.blit(texte_nom,(350,hauteur_fenetre/2+125*(index-3)+20))

	#Méthode permettant d'afficher les appareils
	def consommation(self,liste_consommation,longueur_fenetre,hauteur_fenetre,automate):
		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_consommation = pygame.image.load("carre_appareil.png").convert()

		#On parcourt tous les modes de consommations pour les afficher
		for index,consommation in enumerate(liste_consommation):
			#Initialisation du texte à écrire
			texte_consommation=font.render(str(consommation.conso)+"W -"+str(consommation.conso*100/automate.consommation_globale(liste_consommation))+"%",1,(0,0,0))
			texte_nom=font.render(consommation.nom,1,(0,0,0))

			if consommation.allume==True:
				image_consommation.fill(Color("Green"))
			else:
				image_consommation.fill(Color("Red"))

			#Affichage en fonction de l'index
			self.fenetre.blit(image_consommation,(longueur_fenetre-(index+1)*150,20))
			self.fenetre.blit(texte_consommation,(longueur_fenetre-(index+1)*150,70))
			self.fenetre.blit(texte_nom,(longueur_fenetre-(index+1)*150,30))

	#Méthode permettant d'afficher les stockage
	def stockage(self,liste_stockage,longueur_fenetre,hauteur_fenetre):
		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_stockage = pygame.image.load("carre_stockage.png").convert()

		#On parcourt tous les modes de stockages pour les afficher
		for index,stockage in enumerate(liste_stockage):
			#Initialisation du texte à écrire
			texte_stockage=font.render(str(stockage.stockage)+"/"+str(stockage.capacite),1,(0,0,0))
			texte_nom=font.render(stockage.nom,1,(0,0,0))

			#Affichage en fonction de l'index
			if index < 3:
				self.fenetre.blit(image_stockage,(longueur_fenetre-250,hauteur_fenetre/2+125*index))
				self.fenetre.blit(texte_stockage,(longueur_fenetre-200,hauteur_fenetre/2+125*index+50))
				self.fenetre.blit(texte_nom,(longueur_fenetre-200,hauteur_fenetre/2+125*index+20))
			elif index >= 3:
				self.fenetre.blit(image_stockage,(longueur_fenetre-500,hauteur_fenetre/2+125*(index-3)))
				self.fenetre.blit(texte_stockage,(longueur_fenetre-450,hauteur_fenetre/2+125*(index-3)+50))
				self.fenetre.blit(texte_nom,(longueur_fenetre-450,hauteur_fenetre/2+125*(index-3)+20))


if __name__=='__main__':
	print("Compilation OK")