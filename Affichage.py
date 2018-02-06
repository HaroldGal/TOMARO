#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import Production
import pygame
import random
import time
from pygame.locals import *

#Fonction permettant de renvoyer la coordonnee en x pour centrer un texte en x par rapport à une image
def centrer_texte_x(image,pos_x_image,texte):
	return pos_x_image+image.get_size()[0]/2-texte.get_size()[0]/2

#Transforme les secondes en heures
def decoupe(seconde):
    heure = seconde /3600
    seconde %= 3600
    minute = seconde/60
    seconde%=60
    return (heure,minute,seconde)

#Classe permettant de gérer l'affichage dans une fenetre
class Affichage:
	
	def __init__(self,longueur_fenetre,hauteur_fenetre):
		#Ouverture de la fenêtre Pygame	
		self.fenetre = pygame.display.set_mode((longueur_fenetre,hauteur_fenetre))
		self.fenetre.fill((60,60,100))
		
	#Méthode permettant d'afficher les modes de production
	def production(self,liste_production,longueur_fenetre,hauteur_fenetre,automate):

		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_production = pygame.image.load("Img/carre_production.png").convert()

		#On parcourt tous les modes de productions pour les afficher
		for index,production in enumerate(liste_production):
			#Initialisation du texte à écrire
			texte_production=font.render(str(production.puissance)+"W.h - "+str(int(round(production.puissance*100/(automate.production_globale(liste_production)+1),2)))+"%",1,(0,0,0))
			texte_nom=font.render(production.nom,1,(0,0,0))

			#Affichage en fonction de l'index
			if index < 3:
				self.fenetre.blit(image_production,(50,hauteur_fenetre/2+125*index))
				self.fenetre.blit(texte_production,(centrer_texte_x(image_production,50,texte_production),hauteur_fenetre/2+125*index+50))
				self.fenetre.blit(texte_nom,(centrer_texte_x(image_production,50,texte_nom),hauteur_fenetre/2+125*index+20))
				pygame.draw.line(self.fenetre,Color("Red"),(50+image_production.get_size()[0],hauteur_fenetre/2+125*index+image_production.get_size()[1]/2),(175+image_production.get_size()[0]/2,hauteur_fenetre/2-125+image_production.get_size()[1]),2)
			elif index >= 3:
				self.fenetre.blit(image_production,(300,hauteur_fenetre/2+125*(index-3)))
				self.fenetre.blit(texte_production,(centrer_texte_x(image_production,300,texte_production),hauteur_fenetre/2+125*(index-3)+50))
				self.fenetre.blit(texte_nom,(centrer_texte_x(image_production,300,texte_nom),hauteur_fenetre/2+125*(index-3)+20))
				pygame.draw.line(self.fenetre,Color("Red"),(298,hauteur_fenetre/2+125*(index-3)+image_production.get_size()[1]/2),(175+image_production.get_size()[0]/2,hauteur_fenetre/2-125+image_production.get_size()[1]),2)


	#Méthode permettant d'afficher les appareils
	def consommation(self,liste_consommation,longueur_fenetre,hauteur_fenetre,automate):
		#Taille du texte
		font=pygame.font.Font(None, 25)
		#Chargement de l'image
		image_consommation = pygame.image.load("Img/carre_appareil.png").convert()

		#On parcourt tous les modes de consommations pour les afficher
		for index,consommation in enumerate(liste_consommation):
			#Initialisation du texte à écrire
			if automate.consommation_globale(liste_consommation)!=0 and consommation.allume==True:			
				texte_consommation=font.render(str(consommation.conso)+"W.h - "+str(consommation.conso*100/automate.consommation_globale(liste_consommation))+"%",1,(0,0,0))
			else:
				texte_consommation=font.render(str(consommation.conso)+"W.h - 0%",1,(0,0,0))

			texte_nom=font.render(consommation.nom,1,(0,0,0))

			if consommation.allume==True:
				image_consommation.fill(Color("Green"))
			else:
				image_consommation.fill(Color("Red"))

			#Affichage en fonction de l'index
			self.fenetre.blit(image_consommation,(longueur_fenetre-(index+1)*150,20))
			self.fenetre.blit(texte_consommation,(centrer_texte_x(image_consommation,longueur_fenetre-(index+1)*150,texte_consommation),70))
			self.fenetre.blit(texte_nom,(centrer_texte_x(image_consommation,longueur_fenetre-(index+1)*150,texte_nom),30))



	#Méthode permettant d'afficher les stockage
	def stockage(self,liste_stockage,longueur_fenetre,hauteur_fenetre):
		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_stockage = pygame.image.load("Img/carre_stockage.png").convert()

		#On parcourt tous les modes de stockages pour les afficher
		for index,stockage in enumerate(liste_stockage):
			#Initialisation du texte à écrire
			texte_stockage=font.render(str(stockage.stockage)+"/"+str(stockage.capacite),1,(0,0,0))
			texte_nom=font.render(stockage.nom,1,(0,0,0))

			#Affichage en fonction de l'index
			if index < 3:
				self.fenetre.blit(image_stockage,(longueur_fenetre-250,hauteur_fenetre/2+125*index))
				self.fenetre.blit(texte_stockage,(centrer_texte_x(image_stockage,longueur_fenetre-250,texte_stockage),hauteur_fenetre/2+125*index+50))
				self.fenetre.blit(texte_nom,(centrer_texte_x(image_stockage,longueur_fenetre-250,texte_nom),hauteur_fenetre/2+125*index+20))
			elif index >= 3:
				self.fenetre.blit(image_stockage,(longueur_fenetre-500,hauteur_fenetre/2+125*(index-3)))
				self.fenetre.blit(texte_stockage,(centrer_texte_x(image_stockage,longueur_fenetre-500,texte_stockage),hauteur_fenetre/2+125*(index-3)+50))
				self.fenetre.blit(texte_nom,(centrer_texte_x(image_stockage,longueur_fenetre-500,texte_nom),hauteur_fenetre/2+125*(index-3)+20))

	#Methode permettant d'afficher la fleche correspondante au stockage qu'on charge
	def connexion_stockage(self,index,longueur_fenetre,hauteur_fenetre,couleur):
		image_stockage = pygame.image.load("Img/carre_stockage.png").convert()
		if couleur=="Reset":
			if index < 3:
				pygame.draw.line(self.fenetre,(60,60,100),(longueur_fenetre-250,hauteur_fenetre/2+125*index+image_stockage.get_size()[1]/2),(longueur_fenetre-375+image_stockage.get_size()[0]/2,hauteur_fenetre/2-125+image_stockage.get_size()[1]),2)
			elif index >=3:
				pygame.draw.line(self.fenetre,(60,60,100),(longueur_fenetre-500+image_stockage.get_size()[0],hauteur_fenetre/2+125*(index-3)+image_stockage.get_size()[1]/2),(longueur_fenetre-375+image_stockage.get_size()[0]/2,hauteur_fenetre/2-125+image_stockage.get_size()[1]),2)

		else:
			if index < 3:
				pygame.draw.line(self.fenetre,Color(couleur),(longueur_fenetre-250,hauteur_fenetre/2+125*index+image_stockage.get_size()[1]/2),(longueur_fenetre-375+image_stockage.get_size()[0]/2,hauteur_fenetre/2-125+image_stockage.get_size()[1]),2)
			elif index >=3:
				pygame.draw.line(self.fenetre,Color(couleur),(longueur_fenetre-500+image_stockage.get_size()[0],hauteur_fenetre/2+125*(index-3)+image_stockage.get_size()[1]/2),(longueur_fenetre-375+image_stockage.get_size()[0]/2,hauteur_fenetre/2-125+image_stockage.get_size()[1]),2)



	def prod_stockage_conso_total(self,liste_production,liste_stockage,liste_consommation,automate,longueur_fenetre,hauteur_fenetre):

		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement des images
		image_production = pygame.image.load("Img/carre_production.png").convert()
		image_stockage = pygame.image.load("Img/carre_stockage.png").convert()
		image_consommation = pygame.image.load("Img/carre_appareil.png").convert()

		#Texte pour la production global on affiche sa valeur en watt puis son pourcentage en fonction de l'énergie nécessaire

		if automate.consommation_globale(liste_consommation)!=0:
			texte_production_valeur_globale=font.render(str(automate.production_globale(liste_production))+"W.h - "+str(int(round(automate.production_globale(liste_production)*100/automate.consommation_globale(liste_consommation))))+"%",1,(0,0,0))
		else:
			texte_production_valeur_globale=font.render(str(automate.production_globale(liste_production))+"W.h",1,(0,0,0))

		texte_production_globale=font.render("Production globale",1,(0,0,0))
		self.fenetre.blit(image_production,(175,hauteur_fenetre/2-125))
		self.fenetre.blit(texte_production_valeur_globale,(centrer_texte_x(image_production,175,texte_production_valeur_globale),hauteur_fenetre/2-75))
		self.fenetre.blit(texte_production_globale,(centrer_texte_x(image_production,175,texte_production_globale),hauteur_fenetre/2-105))

		texte_stockage_valeur_globale=font.render(str(automate.stockage_global(liste_stockage)[0])+"/"+str(automate.stockage_global(liste_stockage)[1]),1,(0,0,0))
		texte_stockage_global=font.render("Stockage global",1,(0,0,0))
		self.fenetre.blit(image_stockage,(longueur_fenetre-375,hauteur_fenetre/2-125))
		self.fenetre.blit(texte_stockage_valeur_globale,(centrer_texte_x(image_stockage,longueur_fenetre-375,texte_stockage_valeur_globale),hauteur_fenetre/2-75))
		self.fenetre.blit(texte_stockage_global,(centrer_texte_x(image_stockage,longueur_fenetre-375,texte_stockage_global),hauteur_fenetre/2-105))

		#Reset des fleches
		pygame.draw.polygon(self.fenetre,(60,60,100), ((375+325,hauteur_fenetre/2-100), (375+325, hauteur_fenetre/2-50), (longueur_fenetre/2-150+325,hauteur_fenetre/2-50), (longueur_fenetre/2-150+325, hauteur_fenetre/2-25), (longueur_fenetre/2-100+325, hauteur_fenetre/2-75), (longueur_fenetre/2-150+325, hauteur_fenetre/2-125), (longueur_fenetre/2-150+325,hauteur_fenetre/2-100)))
		pygame.draw.polygon(self.fenetre,(60,60,100), ((longueur_fenetre-376,hauteur_fenetre/2-100), (longueur_fenetre-376, hauteur_fenetre/2-50), (longueur_fenetre/2+150,hauteur_fenetre/2-50), (longueur_fenetre/2+150, hauteur_fenetre/2-25), (longueur_fenetre/2+100, hauteur_fenetre/2-75), (longueur_fenetre/2+150, hauteur_fenetre/2-125), (longueur_fenetre/2+150,hauteur_fenetre/2-100)))

		#Affichage de l'achiminement de l'énergie
		image_acheminement = pygame.image.load("Img/carre_acheminement.png").convert()
		texte_acheminement = font.render("Acheminement",1,(0,0,0))
		if automate.production_globale(liste_production)<automate.consommation_globale(liste_consommation) and automate.stockage_global(liste_stockage)[0]!=0:
			texte_acheminement_etat = font.render("Sous-production",1,(0,0,0))
			pygame.draw.polygon(self.fenetre,Color("Green"), ((longueur_fenetre-376,hauteur_fenetre/2-100), (longueur_fenetre-376, hauteur_fenetre/2-50), (longueur_fenetre/2+150,hauteur_fenetre/2-50), (longueur_fenetre/2+150, hauteur_fenetre/2-25), (longueur_fenetre/2+100, hauteur_fenetre/2-75), (longueur_fenetre/2+150, hauteur_fenetre/2-125), (longueur_fenetre/2+150,hauteur_fenetre/2-100)))

		elif automate.production_globale(liste_production)>automate.consommation_globale(liste_consommation) and automate.stockage_global(liste_stockage)[0]!=automate.stockage_global(liste_stockage)[1]:
			texte_acheminement_etat = font.render("Sur-production",1,(0,0,0))
			pygame.draw.polygon(self.fenetre,Color("Green"), ((375+325,hauteur_fenetre/2-100), (375+325, hauteur_fenetre/2-50), (longueur_fenetre/2-150+325,hauteur_fenetre/2-50), (longueur_fenetre/2-150+325, hauteur_fenetre/2-25), (longueur_fenetre/2-100+325, hauteur_fenetre/2-75), (longueur_fenetre/2-150+325, hauteur_fenetre/2-125), (longueur_fenetre/2-150+325,hauteur_fenetre/2-100)))

		elif automate.production_globale(liste_production)==automate.consommation_globale(liste_consommation):
			texte_acheminement_etat = font.render("Equilibre",1,(0,0,0))

		elif automate.production_globale(liste_production)<automate.consommation_globale(liste_consommation) and automate.stockage_global(liste_stockage)[0]==0:
			texte_acheminement_etat = font.render("Achat",1,(0,0,0))

		elif automate.production_globale(liste_production)>automate.consommation_globale(liste_consommation) and automate.stockage_global(liste_stockage)[0]==automate.stockage_global(liste_stockage)[1]:
			texte_acheminement_etat = font.render("Revente",1,(0,0,0))

		self.fenetre.blit(image_acheminement,(longueur_fenetre/2-100,hauteur_fenetre/2-125))
		self.fenetre.blit(texte_acheminement_etat,(centrer_texte_x(image_acheminement,longueur_fenetre/2-100,texte_acheminement_etat),hauteur_fenetre/2-75))
		self.fenetre.blit(texte_acheminement,(centrer_texte_x(image_acheminement,longueur_fenetre/2-100,texte_acheminement),hauteur_fenetre/2-105))
		
		pygame.draw.polygon(self.fenetre,Color("Red"), ((375,hauteur_fenetre/2-100), (375, hauteur_fenetre/2-50), (longueur_fenetre/2-150,hauteur_fenetre/2-50), (longueur_fenetre/2-150, hauteur_fenetre/2-25), (longueur_fenetre/2-100, hauteur_fenetre/2-75), (longueur_fenetre/2-150, hauteur_fenetre/2-125), (longueur_fenetre/2-150,hauteur_fenetre/2-100)))
		
		#Affichage des traits de connexion entre acheminements et appareils
		for index,appareil in enumerate(liste_consommation):
			#Reset des traits
			#pygame.draw.line(self.fenetre,(60,60,100),(longueur_fenetre/2,hauteur_fenetre/2-125),(longueur_fenetre-(index+1)*150+50,120),2)

			#On dessine la connexion si l'appareil est allumé
			if appareil.allume==True:
				pygame.draw.line(self.fenetre,(240,140,40),(longueur_fenetre/2,hauteur_fenetre/2-126),(longueur_fenetre-(index+1)*150+50,120),2)

	def temps(self,vitesse_temps,nb_seconde):		
		image_temps=pygame.image.load("Img/carre_temps.png").convert()
		self.fenetre.blit(image_temps,(30,20))
		#Taille du texte
		font=pygame.font.Font(None, 25)
		texte_heure = font.render("Heure : "+str(decoupe(nb_seconde)[0])+"h"+str(decoupe(nb_seconde)[1])+"min",1,(0,0,0))#+str(decoupe(nb_seconde)[2])+"s",1,(0,0,0))
		self.fenetre.blit(texte_heure,(centrer_texte_x(image_temps,30,texte_heure),40))

		font=pygame.font.Font(None, 20)		
		texte_tic = font.render("<- Ralentir | -> Accelerer ",1,(0,0,0))#1 TIC = "+str(vitesse_temps)+" s",1,(0,0,0))		
		self.fenetre.blit(texte_tic,(centrer_texte_x(image_temps,30,texte_tic),75))
		texte_pause=font.render("Espace: Pause",1,(0,0,0))
		self.fenetre.blit(texte_pause,(centrer_texte_x(image_temps,30,texte_pause),90))

if __name__=='__main__':
	print("Compilation OK")