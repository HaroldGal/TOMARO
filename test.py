#!/usr/bin/python2.6
# -*-coding:Latin-1 -*

import pygame
import random
import time
from pygame.locals import *

#-----------------VARAIBLE GLOBAL ---------------------#

largeur_fenetre=1200
longueur_fenetre=800

#Appareil
liste_appareil=[]

#Production POUR L'INSTANT UN SEUL MODE (nom,position,production réel))
liste_production=[["Production 1",(largeur_fenetre/3,longueur_fenetre/2),210]]

#Stockage POUR L'INSTANT UN SEUL MODE (nom,position,capacité_max en W,capacité_réel)
liste_stockage=[["Stockage 1",(largeur_fenetre*2/3,longueur_fenetre/2),1000,0],["Stockage 2",(largeur_fenetre*2/3,longueur_fenetre/2+200),1000,0]]

for i in range(0,6):
	#On ajoute à la liste un appareil avec comme caractéristique
	#(nom, position, consommation en W, true=allumé ou false=éteint)
	liste_appareil.append(["Appareil"+str(i+1),(largeur_fenetre-(i+1)*150,20),(i+1)*10,True])


#Fonction permettant d'avoir le total de consommation
def Consomation_Total(liste_appareil):
	consommation_total=0
	for i in range(0,len(liste_appareil)):
		if liste_appareil[i][3] == True:
			consommation_total+=liste_appareil[i][2]

	return consommation_total


#Fonction permettant d'afficher les appareils avec leur nom et donnée de consommation
def Affichage_appareil(liste_appareil,fenetre):

	#Taille du texte
	font=pygame.font.Font(None, 30)
	appareil = pygame.image.load("Img/carre_appareil.png").convert()
	nb_appareil=len(liste_appareil)

	for i in range(0,nb_appareil):
		if liste_appareil[i][3] == True:
			appareil.fill(Color("Green"))
			#Texte de la consomation	
			conso=font.render(str(liste_appareil[i][2]*100/Consomation_Total(liste_appareil))+"%-"+str(liste_appareil[i][2])+"W",1,(0,0,0))				
		else:
			appareil.fill(Color("Red"))
			#Texte de la consomation		
			conso=font.render("0%-"+str(liste_appareil[i][2])+"W",1,(0,0,0))
		
		nom=font.render(liste_appareil[i][0],1,(0,0,0))

		fenetre.blit(appareil,liste_appareil[i][1])
		fenetre.blit(conso,(liste_appareil[i][1][0],liste_appareil[i][1][1]+20))
		fenetre.blit(nom,liste_appareil[i][1])

def Affichage_production(liste_production,fenetre,liste_appareil,liste_stockage):
	#Taille du texte
	font=pygame.font.Font(None, 30)
	production = pygame.image.load("Img/carre_production.png").convert()
	nb_production=len(liste_production)
	for i in range(0,nb_production):
		nb_alea=random.randint(-5,5)
		liste_production[i][2]+=nb_alea
		if Consomation_Total(liste_appareil)!= 0:
			prod=font.render(str(liste_production[i][2])+"W-"+str(liste_production[i][2]*100/Consomation_Total(liste_appareil))+"%",1,(0,0,0))
		else:
			prod=font.render(str(liste_production[i][2])+"W",1,(0,0,0))

		nom=font.render(liste_production[i][0],1,(0,0,0))

		fenetre.blit(production,liste_production[i][1])
		fenetre.blit(prod,(liste_production[i][1][0],liste_production[i][1][1]+20))
		fenetre.blit(nom,liste_production[i][1])
		
		#Si on est en excès de production on remplit le stockage
		if liste_production[i][2]-Consomation_Total(liste_appareil)>0:
			excedant=liste_production[i][2]-Consomation_Total(liste_appareil)
			for i in range(0,len(liste_stockage)):
				#Si le stockage max est pas dépassé
				if liste_stockage[i][3]<=liste_stockage[i][2]:
					liste_stockage[i][3]+=excedant
					#Si après l'ajout le stockage max est toujours pas atteind c'est qu'on a pu tout ajouter, sinon il reste à ajouter l'excedant
					if liste_stockage[i][3]<=liste_stockage[i][2]:
						break
					else:
						excedant=liste_stockage[i][3]-liste_stockage[i][2]
						liste_stockage[i][3]=liste_stockage[i][2]

		#Si on ne produit pas assez on prend dans le stockage
		elif liste_production[i][2]-Consomation_Total(liste_appareil)<0:
			manque=Consomation_Total(liste_appareil)-liste_production[i][2]
			for i in range(0,len(liste_stockage)):
				#S'il y a assez dans le stockage
				if liste_stockage[i][3]>=manque:
					liste_stockage[i][3]-=manque
					#Si après avoir retirer le manque le stockage est toujorus positif c'est qu'on a pris assez sinon il faut prendre dans un autre
					if liste_stockage[i][3]>=0:
						break
					else:
						manque=-liste_stockage[i][3]
						liste_stockage[i][3]=0

def Affichage_stockage(liste_stockage,fenetre):
	#Taille du texte
	font=pygame.font.Font(None, 30)
	stockage = pygame.image.load("Img/carre_stockage.png").convert()
	nb_stockage=len(liste_stockage)

	for i in range(0,nb_stockage):
		capacite=font.render(str(liste_stockage[i][3])+"/"+str(liste_stockage[i][2]),1,(0,0,0))
		nom=font.render(liste_stockage[i][0],1,(0,0,0))

		fenetre.blit(stockage,liste_stockage[i][1])
		fenetre.blit(capacite,(liste_stockage[i][1][0],liste_stockage[i][1][1]+20))
		fenetre.blit(nom,liste_stockage[i][1])

def main():
	pygame.init()

	#Ouverture de la fenêtre Pygame	
	fenetre = pygame.display.set_mode((largeur_fenetre,longueur_fenetre))
	fenetre.fill((60,60,100))

	#Boucle infinie
	continuer=True
	while continuer:
		
		#time.sleep(1)
		nb_appareil=len(liste_appareil)

		#On parcours la liste de tous les événements reçus
		for event in pygame.event.get():   

			#Si un de ces événements est de type QUIT
			if event.type == QUIT:    
				continuer=False;											

			#Si c'est le clic gauche de la souris
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
			  	for i in range(0,nb_appareil):
			  		#Si la souris est sur l'appareil on met l'appareil en allumé ou éteint
			  		if event.pos[0]<liste_appareil[i][1][0]+100 and event.pos[0]>liste_appareil[i][1][0] and event.pos[1]>liste_appareil[i][1][1] and event.pos[1]>liste_appareil[i][1][1]-100:
					    if liste_appareil[i][3]==True:
						    liste_appareil[i][3]=False
					    else:
						    liste_appareil[i][3]=True


		#On reset la fenetre
		fenetre.fill((60,60,100))
		Affichage_appareil(liste_appareil,fenetre)
		Affichage_production(liste_production,fenetre,liste_appareil,liste_stockage)
		Affichage_stockage(liste_stockage,fenetre)
		pygame.display.flip()

main()