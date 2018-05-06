#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from courbe_de_charge import courbe_maj
from Site import *
import calendar
import time
import sys
from Sun import Sun
import pygame
from pygame.locals import *
from Affichage import *

#Transforme les secondes en heures
def decoupe(minute):
    heure = minute /60
    minute %= 60
    return (heure,minute)

#Fonction permettant de dire s'il fait nuit ou pas
def nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords):
	# Heure leve du soleil du jour en minutes
	leve_soleil = int((sun.getSunriseTime( coords, jour_mois, mois, annee )['decimal'] + decalage_horaire)*60)
	# Heure couche du soleil du jour en minutes
	couche_soleil = int((sun.getSunsetTime( coords, jour_mois, mois, annee )['decimal'] + decalage_horaire)*60)

	if(minute_journee > couche_soleil or minute_journee < leve_soleil):
		return True
	else :
		return False

#Renvoie la plage la plus proche en fonction des minutes
def plage_proche(minute,plage):
	new_plage = 0
	diff = 10000
	for p in plage:
		if(abs(minute-p) < diff):
			diff = abs(minute - p)
			new_plage = p
	return new_plage - 1

if(len(sys.argv) != 3):
	print "python deroulement.py nb_foyer affichage_courbe(True ou False)"
	sys.exit()

if(sys.argv[2] != "True" or sys.argv[2] != "False"):
	print "Deuxieme argument inconnu (True ou False)"

#Affichage
largeur_fenetre=1200
longueur_fenetre=800

#Création du site
site_alpha = Site("Campus",int(sys.argv[1]))
#Calcule de la consommation moyenne par jour du site
consommation_moyenne_jour_site = site_alpha.consommation_moyenne_site()

#Variable de temps
plage = [0,360,540,720,900,1080,1260]
str_jour_semaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

#Initialisation de la date du jour
now = time.localtime() 
annee = now.tm_year
mois = 12
jour_mois = now.tm_mday
jour_semaine = now.tm_wday #Lundi 0 .... Dimanche 6
minute_journee = plage_proche(now.tm_hour*60+now.tm_min,plage) #Commence une minute avant un plage existante
site_alpha.actualisation_heure_jour_machine_foyer() #Calcul des horaires pour les différentes machines

# ---------- AJOUTER LATITUDE ET LONGITUDE DE LA VILLE OU VOUS ETES ---------- #
coords = {'longitude' : 2.3522, 'latitude' : 48.8566 }
sun = Sun()
# ---------- AJOUTER LE DECALAGE HORAIRE PAR RAPPORT AU MERIDIEN DE GREENWICH ----------#
decalage_horaire = 1.0

#consommation globale du site
consommation_total = 0

#Gestion de l'affichage
pygame.init()
#Ouverture de la fenêtre Pygame	
fenetre = pygame.display.set_mode((largeur_fenetre,longueur_fenetre))
etat_affichage="menu"

#Stockage
stockage_val=0
stockage_max=10000

#Index du foyer selectionne
index_foyer=-1

#Boucle infinie pour modéliser le temps
continu = True
pause = False
vitesse_sleep=0

while(continu):
	time.sleep(vitesse_sleep)

	#---------- Gestion du temps ----------#	
	
	#Savoir s'il fait nuit ou pas
	is_nuit = nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)
	if(pause!=True):
		minute_journee = minute_journee + 1

	if(minute_journee == 1440):
		jour_semaine += 1
		jour_mois += 1
		minute_journee = 0

	if(jour_semaine == 7):
		jour_semaine = 0

	if(jour_mois > calendar.monthrange(annee,mois)[1]):
		jour_mois = 1
		mois += 1

	if(mois > 12):
		mois = 1
		annee += 1

	##Modification des temps de consommations et déroulement de la journée
	if(minute_journee in plage):
		site_alpha.actualisation_des_plages_h(minute_journee,jour_semaine)

	#Si on est le lundi à minuit on calcul aléatoirement les jours d'allumage des machines des foyers
	if(jour_semaine == 0 and minute_journee == 0):
		site_alpha.actualisation_heure_jour_machine_foyer()

	if minute_journee%60 ==0:
		cle = str("%02d" %jour_mois)+"/"+str("%02d" % mois) + " " + str("%02d" % decoupe(minute_journee)[0]) +":00:00" 
		#print cle
		site_alpha.random_meteo(cle)
		#time.sleep(2)

	site_alpha.actualisation_des_foyers(minute_journee,jour_semaine,is_nuit, cle)

	# print "\033c"	
	# print "Nombre de foyer sur le site:",site_alpha.nb_foyer
	# print "\nNombre d'habitant sur le site:",site_alpha.nb_personne
	# print "\n",decoupe(minute_journee)[0],"h",decoupe(minute_journee)[1],"min -",str_jour_semaine[jour_semaine],"",jour_mois,"/",mois,"/",annee
	# print "\nConsommation globale:",site_alpha.consommation_globale_minute,"W.h"
	# print "\nConsommation moyenne par jour du site:",round(site_alpha.consommation_moyenne_jour/1000),"kW.h"
	# #meteo[temps] = (temperature, rad_globale, rad_directe, rad_diffuse, rad_infrarouge, vitesse_vent)
	# print "\nMeteo à cette heure ci\nTemperature:",str(site_alpha.meteo[cle][0]),"°C - Vent:",str(site_alpha.meteo[cle][5]),"m/s"
	# print "Radiation:\nGlobale:",str(site_alpha.meteo[cle][1]),"Directe:",str(site_alpha.meteo[cle][2]),"Diffuse:",str(site_alpha.meteo[cle][3]),"Infrarouge",str(site_alpha.meteo[cle][4])


	# Affichage du graphique mise à jour toutes les 20 min
	if minute_journee%20 == 0 and sys.argv[2] == "True":
	 	courbe_maj(site_alpha.consommation_globale_minute/1000, minute_journee)

	# elif sys.argv[2] == "False":
	#	time.sleep(0.5)

	#--------------------AFFICHAGE-------------------------#

	#On parcours la liste de tous les événements reçus
	for event in pygame.event.get():   

		#Si un de ces événements est de type QUIT
		if event.type == QUIT:    
			continu=False;

		#Si c'est le clic gauche de la souris
		elif event.type == MOUSEBUTTONDOWN and event.button == 1:
			#Si on est dans le menu
			if(etat_affichage=="menu"):
				#Si on clique sur le bouton pause
				if event.pos[0]>162 and event.pos[0]<180 and event.pos[1]>74 and event.pos[1]<100:
					if pause==True:
						pause=False
					else:
						pause=True

				#Si on clique sur le bouton déccélérer
				elif event.pos[0]>188 and event.pos[0]<235 and event.pos[1]>74 and event.pos[1]<100:
					vitesse_sleep-=0.05
					if vitesse_sleep<0:
						vitesse_sleep=0

				#Si on clique sur le bouton accélérer
				elif event.pos[0]>105 and event.pos[0]<153 and event.pos[1]>74 and event.pos[1]<100:
					vitesse_sleep+=0.05

				#Si on clique sur les foyers
				elif event.pos[0]>72 and event.pos[0]<343 and event.pos[1]>490 and event.pos[1]<630:
					etat_affichage="liste_foyer"

			#Si on est dans liste foyer
			if(etat_affichage=="liste_foyer"):
				if event.pos[0]>0 and event.pos[0]<90 and event.pos[1]>0 and event.pos[1]<90:					
					etat_affichage="menu"

				#Si on clique sur le bouton pause
				elif event.pos[0]>1017 and event.pos[0]<1038 and event.pos[1]>71 and event.pos[1]<99:
					if pause==True:
						pause=False
					else:
						pause=True

				#Si on clique sur le bouton déccélérer
				elif event.pos[0]>1045 and event.pos[0]<1095 and event.pos[1]>71 and event.pos[1]<99:				
					vitesse_sleep-=0.05
					if vitesse_sleep<0:
						vitesse_sleep=0

				#Si on clique sur le bouton accélérer
				elif event.pos[0]>962 and event.pos[0]<1011 and event.pos[1]>72 and event.pos[1]<98:
					vitesse_sleep+=0.05

				#SI ON CLIQUE SUR UN FOYER
				elif event.pos[0]>112 and event.pos[0]<1050 and event.pos[1]>154 and event.pos[1]<600:
					for i in range(0,10):
						if i<5:
							if event.pos[0]>122+i*210 and event.pos[0]<257+i*210 and event.pos[1]>156 and event.pos[1]<290:
								etat_affichage="foyer"
								index_foyer=i
						else:
							if event.pos[0]>122+(i%5)*210 and event.pos[0]<257+(i%5)*210 and event.pos[1]>407 and event.pos[1]<539:
								etat_affichage="foyer"
								index_foyer=i

			#Si on est dans foyer
			if(etat_affichage=="foyer"):
				if event.pos[0]>0 and event.pos[0]<90 and event.pos[1]>0 and event.pos[1]<90:					
					etat_affichage="liste_foyer"

	
	nom_site=site_alpha.nom
	date=str(decoupe(minute_journee)[0])+"h"+str(decoupe(minute_journee)[1])+" - "+str(str_jour_semaine[jour_semaine])+" "+str(jour_mois)+"/"+str(mois)+"/"+str(annee)
	degre=str(site_alpha.meteo[cle][0])
	vent=str(site_alpha.meteo[cle][5])
	localisation="Paris"
	nb_foyer=str(site_alpha.nb_foyer)
	nb_personne=str(site_alpha.nb_personne)
	consommation_totale=str(site_alpha.consommation_globale_minute)
	production_eo= str(site_alpha.eolienne.production_energie(float(site_alpha.meteo[cle][5]))/60.0)
	production_pv= str(site_alpha.panneau.production_energie(float(site_alpha.meteo[cle][1]))/60.0)
	nb_eo=str(site_alpha.eolienne.nb)
	surface_pv=str(site_alpha.panneau.surface)
	production_totale=str(float(production_pv)+float(production_eo))
	if pause!=True and stockage_val<stockage_max:
		stockage_val+=float(production_totale)-float(consommation_totale)
	stockage_val=int(round(min(stockage_max,max(0,stockage_val))))	
	stockage=str(stockage_val)
	stockage_pourcent=str(stockage_val*100/stockage_max)+"%"

	#Si on est dans l'état menu
	if(etat_affichage=="menu"):		
		menu(fenetre,nom_site,date,degre,vent,localisation,nb_foyer,nb_personne,consommation_totale,production_eo,production_pv,production_totale,stockage,stockage_pourcent,is_nuit,nb_eo,surface_pv)

	elif(etat_affichage=="liste_foyer"):
		affichage_liste_foyer(fenetre,site_alpha,date,is_nuit)

	elif(etat_affichage=="foyer"):
		affichage_foyer(fenetre,site_alpha,date,is_nuit,index_foyer)

	pygame.display.flip()

	print "temperature exterieure : ", str(site_alpha.meteo[cle][0])
	print "temperature interieure : ", str(site_alpha.liste_foyer[0].temperature)

