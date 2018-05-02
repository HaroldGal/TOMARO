#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pygame
import random
import time
from pygame.locals import *


#Fonction permettant de renvoyer les coordonnées pour centrer le texte au milieu d'une image
def centrer_texte(image,pos_x_image,pos_y_image,texte):
	return (pos_x_image+image.get_size()[0]/2-texte.get_size()[0]/2,pos_y_image+image.get_size()[1]/2-texte.get_size()[1]/2)

def menu(fenetre,nom_site,date,degre,vent,localisation,nb_foyer,nb_personne,consommation_totale,production_eo,production_pv,production_totale,stockage,is_nuit):	
	#S'il fait jour
	if(is_nuit==False):
		background = pygame.image.load("Image/Background_menu_jour.png").convert()
	else:
		background = pygame.image.load("Image/Background_menu_nuit.png").convert()
	fenetre.blit(background,(0,0))
	#Nom du site
	font=pygame.font.Font(None, 60)	
	nom_site=font.render(nom_site,1,(0,0,0)) #Mettre nom_site
	fenetre.blit(nom_site,(centrer_texte(background,0,0,nom_site)[0],centrer_texte(background,0,0,nom_site)[1]-100))

	#Date
	font=pygame.font.Font(None, 40)
	date=font.render(date,1,(0,0,0)) #Mettre date
	fenetre.blit(date,(20,35))

	#Meteo
	font=pygame.font.Font(None, 25)
	degre_str=font.render(degre,1,(0,0,0))
	vent_str=font.render(vent,1,(0,0,0))
	fenetre.blit(degre_str,(1115-degre_str.get_size()[0],40))
	fenetre.blit(vent_str,(960-vent_str.get_size()[0],40))

	#Localisation
	font=pygame.font.Font(None, 30)
	localisation_str=font.render(localisation,1,(0,0,0))
	fenetre.blit(localisation_str,(630,40))

	#Foyer
	font=pygame.font.Font(None, 30)
	nb_foyer_str=font.render(nb_foyer,1,(0,0,0))
	nb_personne_str=font.render(nb_personne,1,(0,0,0))
	font=pygame.font.Font(None, 40)
	consommation_totale_str=font.render(consommation_totale,1,(0,0,0))
	fenetre.blit(nb_foyer_str,(120-nb_foyer_str.get_size()[0],670))
	fenetre.blit(nb_personne_str,(265-nb_personne_str.get_size()[0],670))
	fenetre.blit(consommation_totale_str,(190-consommation_totale_str.get_size()[0],728))

	#Production
	font=pygame.font.Font(None, 30)
	production_eo_str=font.render(production_eo,1,(0,0,0))
	production_pv_str=font.render(production_pv,1,(0,0,0))
	font=pygame.font.Font(None, 40)
	production_totale_str=font.render(production_totale,1,(0,0,0))
	fenetre.blit(production_eo_str,(695-production_eo_str.get_size()[0],674))
	fenetre.blit(production_pv_str,(515-production_pv_str.get_size()[0],674))
	fenetre.blit(production_totale_str,(610-production_totale_str.get_size()[0],728))

	#Stockage
	font=pygame.font.Font(None, 40)
	stockage_str=font.render(stockage,1,(0,0,0))
	fenetre.blit(stockage_str,(1028-stockage_str.get_size()[0],707))


def affichage_liste_foyer(fenetre,site):
	background = pygame.image.load("Image/Background_liste_foyer.png").convert()
	fenetre.blit(background,(0,0))

	#Affichage nb_personne des 10 premiers foyers
	font=pygame.font.Font(None, 80)
	for i in range(0,10):
		nb_personne=font.render(str(site.liste_foyer[i].nombre_individu),1,(50,59,90))
		if(i==0):
			fenetre.blit(nb_personne,(150,300))
		elif(i==1):
			fenetre.blit(nb_personne,(355,300))
		elif(i==2):
			fenetre.blit(nb_personne,(562,300))
		elif(i==3):
			fenetre.blit(nb_personne,(765,300))
		elif(i==4):
			fenetre.blit(nb_personne,(962,300))
		elif(i==5):
			fenetre.blit(nb_personne,(150,550))
		elif(i==6):
			fenetre.blit(nb_personne,(355,550))
		elif(i==7):
			fenetre.blit(nb_personne,(562,550))
		elif(i==8):
			fenetre.blit(nb_personne,(767,550))
		elif(i==9):
			fenetre.blit(nb_personne,(965,550))


# #Affichage
# largeur_fenetre=1200
# longueur_fenetre=800
# #Gestion de l'affichage
# pygame.init()
# #Ouverture de la fenêtre Pygame	
# fenetre = pygame.display.set_mode((largeur_fenetre,longueur_fenetre))
# background = pygame.image.load("Image/Background.png").convert()
# fenetre.blit(background,(0,0))

# #Boucle infinie pour modéliser le temps
# continu = True
# while(continu):

# 	#On parcours la liste de tous les événements reçus
# 	for event in pygame.event.get():   

# 		#Si un de ces événements est de type QUIT
# 		if event.type == QUIT:    
# 			continu=False;

# 	date="12h50 - Mardi 1 / 5 / 2018"
# 	degre="37.51"
# 	vent="13.51"
# 	localisation="Paris"
# 	nb_foyer="100"
# 	nb_personne="198"
# 	consommation_totale="100009"
# 	production_eo="100000"
# 	production_pv="100000"
# 	production_totale="200000"
# 	stockage="53121/100000"
# 	fenetre.blit(background,(0,0))
# 	menu(fenetre,background,date,degre,vent,localisation,nb_foyer,nb_personne,consommation_totale,production_eo,production_pv,production_totale,stockage)
# 	pygame.display.flip()

