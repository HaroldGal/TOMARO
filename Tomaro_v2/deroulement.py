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

if(len(sys.argv) != 3):
	print "python deroulement.py nb_foyer affichage_courbe(True ou False)"
	sys.exit()

if(sys.argv[2] != "True" or sys.argv[2] != "False"):
	print "Deuxieme argument inconnu (True ou False)"

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
site_alpha.actualisation_heure_jour_machine_foyer() #Calcul des horaires pour les différentes machines

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

	##Modification des temps de consommations et déroulement de la journée
	if(minute_journee in plage):
		site_alpha.actualisation_des_plages_h(minute_journee,jour_semaine)

	#Si on est le lundi à minuit on calcul aléatoirement les jours d'allumage des machines des foyers
	if(jour_semaine == 0 and minute_journee == 0):
		site_alpha.actualisation_heure_jour_machine_foyer()

	site_alpha.actualisation_des_foyers(minute_journee,jour_semaine,is_nuit)

	if minute_journee%60 ==0:
		cle = str("%02d" %jour_mois)+"/"+str("%02d" % mois) + " " + str("%02d" % decoupe(minute_journee)[0]) +":00:00" 
		print cle
		cle = site_alpha.random_meteo(cle)
		time.sleep(2)

	#print "\033c"	
	print "Nombre de foyer sur le site:",site_alpha.nb_foyer
	print "\nNombre d'habitant sur le site:",site_alpha.nb_personne
	print "\n",decoupe(minute_journee)[0],"h",decoupe(minute_journee)[1],"min -",str_jour_semaine[jour_semaine],"",jour_mois,"/",mois,"/",annee
	print "\nConsommation globale:",site_alpha.consommation_globale_minute,"W.h"
	print "\nConsommation moyenne par jour du site:",round(site_alpha.consommation_moyenne_jour/1000),"kW.h"
	#meteo[temps] = (temperature, rad_globale, rad_directe, rad_diffuse, rad_infrarouge, vitesse_vent)
	print "\nMeteo à cette heure ci\nTemperature:",str(site_alpha.meteo[cle][0]),"°C - Vent:",str(site_alpha.meteo[cle][5]),"m/s"
	print "Radiation:\nGlobale:",str(site_alpha.meteo[cle][1]),"Directe:",str(site_alpha.meteo[cle][2]),"Diffuse:",str(site_alpha.meteo[cle][3]),"Infrarouge",str(site_alpha.meteo[cle][4])


	# Affichage du graphique mise à jour toutes les 20 min
	if minute_journee%20 == 0 and sys.argv[2] == "True":
	 	courbe_maj(site_alpha.consommation_globale_minute/1000, minute_journee)

	elif sys.argv[2] == "False":
		time.sleep(0.5)

