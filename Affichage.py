#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import Production
import pygame
import random
import time
from pygame.locals import *

#Classe permettant de gérer l'affichage dans une fenetre
class Affichage:
	
	def __init__(self,hauteur_fenetre,longueur_fenetre):
		#Ouverture de la fenêtre Pygame	
		self.fenetre = pygame.display.set_mode((hauteur_fenetre,longueur_fenetre))
		self.fenetre.fill((60,60,100))
		
	#Méthode permettant d'afficher les modes de production
	def Production(self,liste_production,hauteur_fenetre,longueur_fenetre):

		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_production = pygame.image.load("carre_production.png").convert()

		#On parcourt tous les modes de productions pour les afficher
		for index,production in enumerate(liste_production):
			#Initialisation du texte à écrire
			texte_production=font.render(str(production.energie)+"W",1,(0,0,0))
			texte_nom=font.render(production.nom,1,(0,0,0))

			#Affichage en fonction de l'index
			if index < 3:
				self.fenetre.blit(image_production,(50,longueur_fenetre/2+125*index))
				self.fenetre.blit(texte_production,(100,longueur_fenetre/2+125*index+50))
				self.fenetre.blit(texte_nom,(100,longueur_fenetre/2+125*index+20))
			elif index >= 3:
				self.fenetre.blit(image_production,(300,longueur_fenetre/2+125*(index-3)))
				self.fenetre.blit(texte_production,(350,longueur_fenetre/2+125*(index-3)+50))
				self.fenetre.blit(texte_nom,(350,longueur_fenetre/2+125*(index-3)+20))
			#fenetre.blit(prod,(liste_production[i][1][0],liste_production[i][1][1]+20))
			#fenetre.blit(nom,liste_production[i][1])










if __name__=='__main__':
	print("Compilation OK")