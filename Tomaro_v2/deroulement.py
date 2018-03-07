#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from Site import *
import time

#Création du site
site_alpha = Site("Campus",1000)


#Variable de temps
plage = [0,360,540,720,900,1080,1260]
annee = 0
semaine = 0
jour_semaine = 0 #Lundi 0 .... Dimanche 6
minute_journee = 0

#Boucle infinie pour modéliser le temps
continu = True
while(continu):
	#time.sleep(1)

	if(minute_journee in plage):
		site_alpha.actualisation_des_plages_h(minute_journee,jour_semaine)

	site_alpha.actualisation_des_foyers(minute_journee)

	#---------- Gestion du temps ----------#
	minute_journee = minute_journee + 1
	if(minute_journee%1440 == 0 and minute_journee!=0):
		jour_semaine = jour_semaine + 1
		minute_journee = 0
	if(jour_semaine%7 == 0 and jour_semaine!=0):
		semaine = semaine + 1
		jour_semaine = 0
	if(semaine%52 == 0 and semaine!=0):
		annee = annee + 1
		semaine = 0

	print minute_journee,"min",jour_semaine,"jour",semaine,"semaine"

