#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import Consommation
#import Production
#import Stockage
from Affichage import Affichage
from Production import *
import pygame
import random
import time
from pygame.locals import *

hauteur_fenetre=1200
longueur_fenetre=800

#Initialisation de Pygame et de la fenetre
pygame.init()
affichage=Affichage(hauteur_fenetre,longueur_fenetre)

#Initialisation de la liste des appareils
liste_production=[]
Prod1=Production("Prod1")
liste_production.append(Prod1)
Prod2=Production("Prod2")
liste_production.append(Prod2)
liste_production.append(Prod2)
liste_production.append(Prod2)
liste_production.append(Prod2)
liste_production.append(Prod2)


#Boucle infinie
continuer=True
while continuer:

	#On parcours la liste de tous les événements reçus
	for event in pygame.event.get():   

		#Si un de ces événements est de type QUIT
		if event.type == QUIT:    
			continuer=False

	affichage.Production(liste_production,hauteur_fenetre,longueur_fenetre)

	pygame.display.flip()