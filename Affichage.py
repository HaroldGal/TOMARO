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
		image_production = pygame.image.load("carre_production.png").convert()

		#On parcourt tous les modes de productions pour les afficher
		for index,production in enumerate(liste_production):
			#Initialisation du texte à écrire
			texte_production=font.render(str(production.energie)+"W - "+str(production.energie*100/automate.production_globale(liste_production))+"%",1,(0,0,0))
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
				pygame.draw.line(self.fenetre,Color("Red"),(300,hauteur_fenetre/2+125*(index-3)+image_production.get_size()[1]/2),(175+image_production.get_size()[0]/2,hauteur_fenetre/2-125+image_production.get_size()[1]),2)


	#Méthode permettant d'afficher les appareils
	def consommation(self,liste_consommation,longueur_fenetre,hauteur_fenetre,automate):
		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement de l'image
		image_consommation = pygame.image.load("carre_appareil.png").convert()

		#On parcourt tous les modes de consommations pour les afficher
		for index,consommation in enumerate(liste_consommation):
			#Initialisation du texte à écrire
			texte_consommation=font.render(str(consommation.conso)+"W - "+str(consommation.conso*100/automate.consommation_globale(liste_consommation))+"%",1,(0,0,0))
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
		image_stockage = pygame.image.load("carre_stockage.png").convert()

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
		image_stockage = pygame.image.load("carre_stockage.png").convert()
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



	def prod_stockage_conso_total(self,liste_production,liste_stockage,liste_consommation,automate,longueur_fenetre,hauteur_fenetre,etat_production):

		#Taille du texte
		font=pygame.font.Font(None, 30)
		#Chargement des images
		image_production = pygame.image.load("carre_production.png").convert()
		image_stockage = pygame.image.load("carre_stockage.png").convert()
		image_consommation = pygame.image.load("carre_appareil.png").convert()

		#Texte pour la production global on affiche sa valeur en watt puis son pourcentage en fonction de l'énergie nécessaire
		texte_production_valeur_globale=font.render(str(automate.production_globale(liste_production))+"W - "+str(automate.production_globale(liste_production)*100/automate.consommation_globale(liste_consommation))+"%",1,(0,0,0))
		texte_production_globale=font.render("Production globale",1,(0,0,0))
		self.fenetre.blit(image_production,(175,hauteur_fenetre/2-125))
		self.fenetre.blit(texte_production_valeur_globale,(centrer_texte_x(image_production,175,texte_production_valeur_globale),hauteur_fenetre/2-75))
		self.fenetre.blit(texte_production_globale,(centrer_texte_x(image_production,175,texte_production_globale),hauteur_fenetre/2-105))

		texte_stockage_valeur_globale=font.render(str(automate.stockage_global(liste_stockage)[0])+"/"+str(automate.stockage_global(liste_stockage)[1]),1,(0,0,0))
		texte_stockage_global=font.render("Stockage global",1,(0,0,0))
		self.fenetre.blit(image_stockage,(longueur_fenetre-375,hauteur_fenetre/2-125))
		self.fenetre.blit(texte_stockage_valeur_globale,(centrer_texte_x(image_stockage,longueur_fenetre-375,texte_stockage_valeur_globale),hauteur_fenetre/2-75))
		self.fenetre.blit(texte_stockage_global,(centrer_texte_x(image_stockage,longueur_fenetre-375,texte_stockage_global),hauteur_fenetre/2-105))

		#Si la production globale est plus grande que la consommation alors on fait un lien entre la production globale et le stockage global
		



if __name__=='__main__':
	print("Compilation OK")