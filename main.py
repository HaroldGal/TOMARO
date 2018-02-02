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


#Boucle infinie
continuer=True
while continuer:

	#Permet de gérer le temps car sinon ca va trop trop vite
	#time.sleep(0.5)

	#On parcours la liste de tous les événements reçus
	for event in pygame.event.get():   

		#Si un de ces événements est de type QUIT
		if event.type == QUIT:    
			continuer=False


	modif_prod(liste_production)
	#etat_production récupère si on est en "surplus" ou "manque" en fonction de cette valeur l'affichage affichera une fleche dans un sens ou un autre
	etat_production=automate.gestion_du_stockage(liste_production, liste_stockage, liste_consommation,affichage,longueur_fenetre,hauteur_fenetre)
	affichage.production(liste_production,longueur_fenetre,hauteur_fenetre,automate)
	affichage.consommation(liste_consommation,longueur_fenetre,hauteur_fenetre,automate)
	affichage.stockage(liste_stockage,longueur_fenetre,hauteur_fenetre)
	affichage.prod_stockage_conso_total(liste_production,liste_stockage,liste_consommation,automate,longueur_fenetre,hauteur_fenetre,etat_production)

	
	pygame.display.flip()
