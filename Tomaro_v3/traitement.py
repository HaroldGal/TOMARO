#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from pretraitement import *
import sys
from random import seed

#Transforme les secondes en heures
def decoupe(minute):
    heure = minute /60
    minute %= 60
    if heure == 24:
    	return(0,minute)
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

stock = 0

def prod_conso2(jour_annee, stock):
#---- ON SIMULE LES DONNES SUR UN AN POUR AVOIR LA CONSOMMATION MOYENNE "U" LA PRODUCTION SOLAIRE "X" ET EOLIENNE "Y" CHAQUE JOUR

	#time.sleep(0.5)

	#---------- Gestion du temps ----------#
	date = datetime.datetime.strptime(str(jour_annee), '%j').strftime('%d/%m')
	jour_mois=int(date[0:2])
	mois = int(date[3:5])
	minute_journee = 0
	annee = 1
	jour_semaine = jour_annee%7 #Lundi 0 .... Dimanche 6
	conso_jour=0
	PV1.production_energie_jour = 0
	EO1.production_energie_jour = 0
	achat = 0
	vente = 0
	stock_max = 13000*1
	prod_h = 0

	# print "jour_semaine=",jour_semaine,"jour_mois=",jour_mois,"mois=",mois

	while(minute_journee<=1440):
		#Savoir s'il fait nuit ou pas
		is_nuit = nuit(minute_journee, jour_mois, mois, annee, decalage_horaire, coords)
		
		##Modification des temps de consommations et déroulement de la journée
		if(minute_journee in plage):
			site_alpha.actualisation_des_plages_h(minute_journee,jour_semaine)

		#Si on est le lundi à minuit on calcul aléatoirement les jours d'allumage des machines des foyers
		if(jour_semaine == 0 and minute_journee == 0):
			site_alpha.actualisation_heure_jour_machine_foyer()

		cle = str("%02d" %jour_mois)+"/"+str("%02d" % mois) + " " + str("%02d" % decoupe(minute_journee)[0]) +":00:00"
		site_alpha.actualisation_des_foyers(minute_journee,jour_semaine,is_nuit,cle)

		if minute_journee%60 ==0:		
			# cle = str("%02d" %jour_mois)+"/"+str("%02d" % mois) + " " + str("%02d" % decoupe(minute_journee)[0]) +":00:00"
			site_alpha.random_meteo(cle)
			# print cle
			PV1.production_energie_jour = 0
			EO1.production_energie_jour = 0
			PV1.production_energie(float(site_alpha.meteo[cle][1]))
			EO1.production_energie(float(site_alpha.meteo[cle][5]))
			prod_h = PV1.production_energie_jour+EO1.production_energie_jour



		conso_jour+=site_alpha.consommation_globale_minute
		if site_alpha.consommation_globale_minute < prod_h/60 :
			stock += prod_h/60 - site_alpha.consommation_globale_minute
		else:
			achat += site_alpha.consommation_globale_minute - prod_h/60

		if stock > stock_max:
			vente += stock - stock_max
			stock = stock_max


		minute_journee = minute_journee + 1

	return (achat, vente, stock)



if __name__ == '__main__':
	seed(4)

	print "longueur=", len(sys.argv)

	# if(len(sys.argv) < 2):
	# 	print "python deroulement.py nb_foyer affichage_courbe(True ou False)"
	# 	sys.exit()

	nb_Pv = int(sys.argv[1])
	nb_Eo = int(sys.argv[2])

	#Création du site
	site_alpha = Site("Campus",int(sys.argv[1]),nb_Eo,nb_Pv)
	#Calcule de la consommation moyenne par jour du site
	consommation_moyenne_jour_site = site_alpha.consommation_moyenne_site()

	#Variable de temps
	plage = [0,360,540,720,900,1080,1260]
	str_jour_semaine = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

	#Initialisation de la date du jour 

	#-------ON COMMENCE LE 01/01/01 à 00h00
	now = time.time() 
	annee = 1 
	mois = 1
	jour_mois = 1
	jour_semaine = 0 #Lundi 0 .... Dimanche 6
	minute_journee = 0
	site_alpha.actualisation_heure_jour_machine_foyer() #Calcul des horaires pour les différentes machines

	# ---------- AJOUTER LATITUDE ET LONGITUDE DE LA VILLE OU VOUS ETES ---------- #
	coords = {'longitude' : 2.3522, 'latitude' : 48.8566 }
	sun = Sun()

	# ---------- AJOUTER LE DECALAGE HORAIRE PAR RAPPORT AU MERIDIEN DE GREENWICH ----------#
	decalage_horaire = 1.0

	#consommation globale du site
	consommation_total = 0

	#Producion
	PV1 = PV(0.18,nb_Pv,0.8) #http://www.photovoltaique-energie.fr/estimer-la-production-photovoltaique.html
	EO1 = EO(13,nb_Eo,0.15) #https://www.alma-solarshop.fr/panneau-bisol/733-panneau-bisol-bmo-280-noir.html

	cle = str("%02d" %jour_mois)+"/"+str("%02d" % mois) + " " + str("%02d" % decoupe(minute_journee)[0]) +":00:00"
	cle = site_alpha.random_meteo(cle)
	
	tab_consomation_jour = []

	tab_consomation_jour.append(prod_conso2(1,0))
	for i in range(2,360):
		tab_consomation_jour.append(prod_conso2(i,tab_consomation_jour[i-2][2]))

	achat_glob = 0
	vente_glob = 0

	for jour in tab_consomation_jour:
		achat_glob += jour[0]
		vente_glob += jour[1]
	print "Bilan énergétique: "
	print "Achat : ", achat_glob/100.0, "kW"
	print "Vente : ", vente_glob/100.0, "kW"
