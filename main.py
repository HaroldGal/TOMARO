#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#import Consommation
#import Production
#import Stockage
from Affichage import *
from Production import *
from Consommation import *
from Stockage import *
from Automate import *
import pygame
import random
import time
from pygame.locals import *
import matplotlib.pyplot as plt

def creation_appareil(nom_file):
	liste_appareil = []
	fichier = open(nom_file,"r")
	for ligne in fichier:
		dataApp = ligne.split(":")
		#print (dataApp[0])
		liste_appareil.append(Appareil(dataApp[0], int(float(dataApp[1])*1000), dataApp[2]))

	return liste_appareil
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

def modif_conso(liste_appareil,nb_seconde):

	for appareil in liste_appareil:
		if appareil.tableaubinaire[nb_seconde]=="1":
			appareil.allume=True
		else :
			appareil.allume=False
hauteur_fenetre=800
longueur_fenetre=1200

#Initialisation de Pygame et de la fenetre
pygame.init()
affichage=Affichage(longueur_fenetre,hauteur_fenetre)

#Initialisation de l'automate
automate=Automate()

# tableau consommation globale pour la courbe de charge
consommation_globale_courbe = []
tableau_temps_min=[]
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
liste_consommation=creation_appareil("testconso.txt")
"""
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
"""
#Initialisation de la liste des stockages 6 MAX !!!
liste_stockage=[]
Stockage1=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage1)
Stockage2=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage2)
Stockage3=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage3)
Stockage4=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage4)
Stockage5=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage5)
Stockage6=Stockage("PowerWall",3500,0.9,20)
liste_stockage.append(Stockage6)

#Controle de la vitesse
vitesse_temps=1
nb_seconde=0

#Boucle infinie
pause=False
continuer=True
while continuer:
	#On parcours la liste de tous les événements reçus
	for event in pygame.event.get():   

		#Si un de ces événements est de type QUIT
		if event.type == QUIT:    
			continuer=False

		elif event.type == KEYDOWN:
			if event.key == K_SPACE: #Permet de faire pause
				if pause==True:
					pause=False
				else:
					pause=True
			elif event.key == K_RIGHT:	
				if vitesse_temps >= 0.1:			
					vitesse_temps-=0.1		
				if vitesse_temps < 0.1:
					vitesse_temps=0	

			elif event.key == K_LEFT:
				vitesse_temps+=0.1

	if pause==False:
		#Refresh la fenetre
		affichage.fenetre.fill((60,60,100))

		#Permet de gérer le temps car sinon ca va trop trop vite
		time.sleep(vitesse_temps)

		nb_seconde+=60
		nb_seconde=nb_seconde%(24*60*60)
					
		#FONCTION DE MODIFICATION DE LA PRODUCTION EN FONCTION DU TEMPS ICI
		modif_conso(liste_consommation,nb_seconde)
		consommation_globale_courbe.append(automate.consommation_globale(liste_consommation))
		tableau_temps_min.append(decoupe(nb_seconde)[0])
		#FONCTION DE MODIFICATION DE LA CONSOMMATION EN FONCTION DU TEMPS ICI
	   
		modif_prod(liste_production) #POUR TEST A RETIRE QUAND FONCTION DE MODIF DE PRODUCTION FAITE

		#FONCTION DE GESTION DU STOCKAGE
		automate.gestion_du_stockage(liste_production, liste_stockage, liste_consommation,affichage,longueur_fenetre,hauteur_fenetre)
		
		#GESTION DE L'AFFICHAGE	
		affichage.production(liste_production,longueur_fenetre,hauteur_fenetre,automate)
		affichage.consommation(liste_consommation,longueur_fenetre,hauteur_fenetre,automate)
		affichage.stockage(liste_stockage,longueur_fenetre,hauteur_fenetre)
		affichage.prod_stockage_conso_total(liste_production,liste_stockage,liste_consommation,automate,longueur_fenetre,hauteur_fenetre)
		affichage.temps(vitesse_temps,nb_seconde)

		
		pygame.display.flip()

#Permet d'avoir le résultat à la fin
print "Manque d'énergie "+str(automate.tic_energie_manquante*100/automate.tic_total)+"%"+" du temps"
plt.plot(tableau_temps_min,consommation_globale_courbe)
plt.ylabel('Consommation globale du site en W')
plt.xlabel('Temps en heure')
plt.savefig('Results/courbe_de_charge.png')
