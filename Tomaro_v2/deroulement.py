#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from courbe_de_charge import courbe_maj
from Site import *
import calendar
import time
import sys
from Sun import Sun

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
mois = now.tm_mon
jour_mois = now.tm_mday
jour_semaine = now.tm_wday #Lundi 0 .... Dimanche 6
minute_journee = plage_proche(now.tm_hour*60+now.tm_min,plage) #Commence une minute avant un plage existante

# ---------- AJOUTER LATITUDE ET LONGITUDE DE LA VILLE OU VOUS ETES ---------- #
coords = {'longitude' : 2.3522, 'latitude' : 48.8566 }
sun = Sun()
# ---------- AJOUTER LE DECALAGE HORAIRE PAR RAPPORT AU MERIDIEN DE GREENWICH ----------#
decalage_horaire = 1.0

#consommation globale du site
consommation_total = 0

#Boucle infinie pour modéliser le temps
continu = True
while(continu):

	#time.sleep(0.5)

	#---------- Gestion du temps ----------#	
	
	#Savoir s'il fait nuit ou pas
	is_nuit = nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)
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

	#Déroulement de la journée
	if(minute_journee in plage):
		site_alpha.actualisation_des_plages_h(minute_journee,jour_semaine)

	site_alpha.actualisation_des_foyers(minute_journee,is_nuit)

	print "\033c"	
	print "Nb_habitant =",site_alpha.nb_personne
	print decoupe(minute_journee)[0],"h",decoupe(minute_journee)[1],"min -",str_jour_semaine[jour_semaine],"",jour_mois,"/",mois,"/",annee
	print "Consommation globale =",site_alpha.consommation_globale_minute/1000,"kW.h"

	#Affichage du graphique mise à jour toutes les 20 min
	if minute_journee%20 ==0:
		courbe_maj(site_alpha.consommation_globale_minute, minute_journee)

