#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from courbe_de_charge import courbe_maj
from Site import *
import calendar
import time
import datetime
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
		return (True,leve_soleil,couche_soleil)
	else :
		return (False,leve_soleil,couche_soleil)

#Renvoie la plage la plus proche en fonction des minutes
def plage_proche(minute,plage):
	new_plage = 0
	diff = 10000
	for p in plage:
		if(abs(minute-p) < diff):
			diff = abs(minute - p)
			new_plage = p
	return new_plage - 1

if(len(sys.argv) != 2 and len(sys.argv) != 3):
	print "python deroulement.py nb_foyer jour/mois/annee"
	sys.exit()



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
str_mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]

#Initialisation de la date du jour si pas d'argument
now = time.localtime() 
if(len(sys.argv) == 2):	
	
	annee = now.tm_year
	mois = now.tm_mon
	jour_mois = now.tm_mday
	jour_semaine = now.tm_wday #Lundi 0 .... Dimanche 6

elif(len(sys.argv) == 3):
	annee=int(sys.argv[2].split('/')[2])
	mois=int(sys.argv[2].split('/')[1])
	jour_mois=int(sys.argv[2].split('/')[0])
	jour_semaine = datetime.datetime(annee,mois,jour_mois,0,0,0).weekday() #Lundi 0 .... Dimanche 6

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

#AFFICHAGE
#Index du foyer selectionne
index_foyer=-1
liste_objet=[]

#Boucle infinie pour modéliser le temps
continu = True
pause = False
vitesse_sleep=0

while(continu):
	time.sleep(vitesse_sleep)

	#---------- Gestion du temps ----------#	
	
	#Savoir s'il fait nuit ou pas
	is_nuit = nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)[0]
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
		site_alpha.random_meteo(cle)


	site_alpha.actualisation_des_foyers(minute_journee,jour_semaine,is_nuit, cle)

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

				#Si on clique quelque part dans la maison on voit ou précisement pour avoir la part de conso de l'objet dans la maison
				elif event.pos[0]>214 and event.pos[0]<964 and event.pos[1]>48 and event.pos[1]<724:
					#Lampe
					if event.pos[0]>374 and event.pos[0]<374+35 and event.pos[1]>283 and event.pos[1]<283+40:
						if ("lampe",0) not in liste_objet:
							liste_objet=[]
							liste_objet.append(("lampe",0))
						elif ("lampe",0) in liste_objet:
							liste_objet.remove(("lampe",0))
					elif event.pos[0]>780 and event.pos[0]<780+35 and event.pos[1]>283  and event.pos[1]<283+40:
						if ("lampe",1) not in liste_objet:
							liste_objet=[]
							liste_objet.append(("lampe",1))
						elif ("lampe",1) in liste_objet:
							liste_objet.remove(("lampe",1))
					elif event.pos[0]>374 and event.pos[0]<374+35 and event.pos[1]>399 and event.pos[1]<399+40:
						if ("lampe",2) not in liste_objet:
							liste_objet=[]
							liste_objet.append(("lampe",2))
						elif ("lampe",2) in liste_objet:
							liste_objet.remove(("lampe",2))
					elif event.pos[0]>780 and event.pos[0]<780+35 and event.pos[1]>399 and event.pos[1]<399+40:
						if ("lampe",3) not in liste_objet:
							liste_objet=[]
							liste_objet.append(("lampe",3))
						elif ("lampe",3) in liste_objet:
							liste_objet.remove(("lampe",3))



	if(pause!=True):
		nom_site=site_alpha.nom
		date=str(decoupe(minute_journee)[0])+"h"+str(decoupe(minute_journee)[1])+" - "+str(str_jour_semaine[jour_semaine])+" "+str(jour_mois)+" "+str_mois[mois-1]+" "+str(annee)
		degre=str(site_alpha.meteo[cle][0])
		vent=str(site_alpha.meteo[cle][5])
		localisation= "Paris"
		nb_foyer=str(site_alpha.nb_foyer)
		nb_personne=str(site_alpha.nb_personne)
		consommation_totale=str(site_alpha.consommation_globale_minute)
		production_eo= str(int(round(site_alpha.eolienne.production_energie(float(site_alpha.meteo[cle][5]))/60.0)))
		production_pv= str(int(round(site_alpha.panneau.production_energie(float(site_alpha.meteo[cle][1]))/60.0)))
		nb_eo=str(site_alpha.eolienne.nb)
		surface_pv=str(site_alpha.panneau.surface)
		production_totale=str(int(round(float(production_pv)+float(production_eo))))	
		if pause!=True and stockage_val<stockage_max:
			stockage_val+=float(production_totale)-float(consommation_totale)
		stockage_val=int(round(min(stockage_max,max(0,stockage_val))))	
		stockage=str(stockage_val)
		stockage_pourcent=str(stockage_val*100/stockage_max)+"%"
		temps_jour=nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)[2]-nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)[1]
		temps_nuit=1440-temps_jour
		minute_leve=nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)[1]
		minute_couche=nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)[2]
		#Si on est dans l'état menu
		if(etat_affichage=="menu"):		
			menu(fenetre,nom_site,date,degre,vent,localisation,nb_foyer,nb_personne,consommation_totale,production_eo,production_pv,production_totale,stockage,stockage_pourcent,is_nuit,nb_eo,surface_pv,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche)

		elif(etat_affichage=="liste_foyer"):
			affichage_liste_foyer(fenetre,site_alpha,date,is_nuit,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche)

		elif(etat_affichage=="foyer"):
			affichage_foyer(fenetre,site_alpha,date,is_nuit,index_foyer,degre,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche,liste_objet)

		pygame.display.flip()

	#print "temperature exterieure : ", str(site_alpha.meteo[cle][0])
	#print "temperature interieure : ", str(site_alpha.liste_foyer[0].temperature)

