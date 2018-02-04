#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import Consommation
#import Production
#import Stockage
from Affichage import Affichage
from Production import *
from Consommation import *
from Stockage import *
from Automate import *
import pygame
import random
import time
from pygame.locals import *


def creation_appareil(nom_file):
	liste_appareil = []
	fichier = open(nom_file,"r")
	for ligne in fichier:
		dataApp = ligne.split(" ")
		liste_appareil.append(Appareil(dataApp[0], dataApp[1], dataApp[2:end]))

	fichier.close()

#FONCTION POUR LES TEST A ENLEVER QUI MODIFIE LA PRODUCTION EN AJOUTANT +-[-5,5] chaque tour à chaque appareil
def modif_prod(liste_production):

	for production in liste_production:
		nb_alea=random.randint(-5,5)
		production.energie+=nb_alea
		if production.energie < 0:
			production.energie=0
		elif production.energie>100:
			production.energie=100


hauteur_fenetre=800
longueur_fenetre=1200

#Initialisation de Pygame et de la fenetre
pygame.init()
affichage=Affichage(longueur_fenetre,hauteur_fenetre)

#Initialisation de l'automate
automate=Automate()

#Initialisation de la liste des appareils 6 MODE DE PRODUCTION MAX !!!
liste_production=[]
Prod1=Production("Prod1")
liste_production.append(Prod1)
Prod2=Production("Prod2")
liste_production.append(Prod2)
Prod3=Production("Prod3")
liste_production.append(Prod3)
Prod4=Production("Prod4")
liste_production.append(Prod4)
Prod5=Production("Prod5")
liste_production.append(Prod5)
Prod6=Production("Prod6")
liste_production.append(Prod6)

#Initialisaiton de la liste des appareils 7 MAX !!!
liste_consommation=[]
Appareil1=Appareil("Appareil1",50)
liste_consommation.append(Appareil1)
Appareil2=Appareil("Appareil2",50)
liste_consommation.append(Appareil2)
Appareil3=Appareil("Appareil3",50)
liste_consommation.append(Appareil3)
Appareil4=Appareil("Appareil4",50)
liste_consommation.append(Appareil4)
Appareil5=Appareil("Appareil5",50)
liste_consommation.append(Appareil5)
Appareil6=Appareil("Appareil6",50)
liste_consommation.append(Appareil6)

#Initialisation de la liste des stockages 6 MAX !!!
liste_stockage=[]
Stockage1=Stockage("Stockage1",1000,0.9,20)
liste_stockage.append(Stockage1)
Stockage2=Stockage("Stockage2",1000,0.9,20)
liste_stockage.append(Stockage2)
Stockage3=Stockage("Stockage3",1000,0.9,20)
liste_stockage.append(Stockage3)
Stockage4=Stockage("Stockage4",1000,0.9,20)
liste_stockage.append(Stockage4)
Stockage5=Stockage("Stockage5",1000,0.9,20)
liste_stockage.append(Stockage5)
Stockage6=Stockage("Stockage6",1000,0.9,20)
liste_stockage.append(Stockage6)

#Controle de la vitesse
vitesse_temps=0
affichage.temps(vitesse_temps,False)

#Boucle infinie
continuer=True
while continuer:

	#Permet de gérer le temps car sinon ca va trop trop vite
	time.sleep(vitesse_temps)


	#On parcours la liste de tous les événements reçus
	for event in pygame.event.get():   

		#Si un de ces événements est de type QUIT
		if event.type == QUIT:    
			continuer=False

		#TEST POUR VOIR QUAND UN APPAREIL SETEINT, A ENLEVER
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				for index,appareil in enumerate(liste_consommation):
					if appareil.allume==True:
						appareil.allume=False
					else:
						appareil.allume=True
			elif event.key == K_UP:
				if vitesse_temps>0.05:
					affichage.temps(vitesse_temps,True)
					vitesse_temps-=0.05
				elif vitesse_temps==0.05:
						vitesse_temps=0				
				
				elif vitesse_temps==0:
					print "Vitesse max atteinte"

				if vitesse_temps < 0.05:
					vitesse_temps=0

				affichage.temps(vitesse_temps,False)

			elif event.key == K_DOWN:
				affichage.temps(vitesse_temps,True)
				vitesse_temps+=0.05
				affichage.temps(vitesse_temps,False)

	#FONCTION DE MODIFICATION DE LA PRODUCTION EN FONCTION DU TEMPS ICI

	#FONCTION DE MODIFICATION DE LA CONSOMMATION EN FONCTION DU TEMPS ICI

	modif_prod(liste_production) #POUR TEST A RETIRE QUAND FONCTION DE MODIF DE PRODUCTION FAITE

	#GESTION DE L'AFFICHAGE	
	affichage.production(liste_production,longueur_fenetre,hauteur_fenetre,automate)
	affichage.consommation(liste_consommation,longueur_fenetre,hauteur_fenetre,automate)
	affichage.stockage(liste_stockage,longueur_fenetre,hauteur_fenetre)
	affichage.prod_stockage_conso_total(liste_production,liste_stockage,liste_consommation,automate,longueur_fenetre,hauteur_fenetre)

	
	pygame.display.flip()
