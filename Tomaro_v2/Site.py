#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from Foyer import *
from Production import *
from random import randrange,sample, randint
from math import sqrt

lien_data_meteo = "Data/meteo.csv"

class Site:

	def __init__(self, nom, nb_foyer):

		self.nom = nom
		self.nb_foyer = nb_foyer
		self.consommation_globale_minute = 0	
		self.variation_temp = 0
		self.variation_temp_frigo = 0

		#Initialisation de la liste des foyers
		self.liste_foyer = self.init_liste_foyer(nb_foyer)

		#Initialisaiton de la liste des productions
		self.eolienne, self.panneau = self.init_production()

		#Initialisation de la liste des stockages
		self.liste_stockage = self.init_liste_stockage()

		#Nombre d'habitant du site
		self.nb_personne = self.compteur_personne()

		#Les donnees meteo du site pendant une année
		self.meteo = self.init_meteo()
		#dictionnaire de la forme
		#meteo[temps] = (temperature, rad_globale, rad_directe, rad_diffuse, rad_infrarouge, vitesse_vent)
		#temps sous la forme "dd/mm hh:mm:ss"

		#Consommation moyenne du site par jour
		self.consommation_moyenne_jour = self.consommation_moyenne_site()
		self.lamb = 0.05 # un materiaux est dit isolant si lambda < 0.065
		self.capa = 1256.0
		
	#Fonction permettant de renvoyer la liste avec tous les foyers du site
	def init_liste_foyer(self, nb_foyer):

		liste_foyer = []
		#Chaque foyer à 4 personnes max
		for i in range(0,nb_foyer):
			print "\033c"
			print str(i*100/nb_foyer)+"%"
			liste_foyer.append(Foyer(randrange(1,5)))

		return liste_foyer

	def init_meteo(self):
		print "Creation de la base de donnee meteo"
		meteo = dict()
		with open(lien_data_meteo, 'rb') as FichierCsv:
			lignes = csv.reader(FichierCsv, delimiter=',')
			next(lignes,None)
			for line in lignes:
				meteo[line[0][0:5] + line[0][10:]] = (line[1], line[2], line[3], line[4], line[5], line[6])

		print "Donnees meteo complete"
		return meteo
		
	def random_meteo(self, cle):
		jour = int(cle[0:2])
		mois = int(cle[3:5])

		jour = randint(jour-15,jour+15)
		if mois == 2:
			if jour<=0:
				jour = jour+31
				mois-=1				
			elif jour>28:
				jour = jour%28
				mois+=1
		else:
			if jour<=0:
				jour = jour+28
				mois-=1
			elif jour>30:
				jour = jour%28
				mois+=1
		if mois == 0:
			mois = 12
		if mois == 13:
			mois = 1

		#print str("%02d" %jour) + '/' + str("%02d" %mois) + cle[5:]
		#dd/mm hh:mm:ss"
		#print cle
		if(cle[6:8]!="00"):
			choix_random = str("%02d" %jour) + '/' + str("%02d" %mois) + cle[5:]
			choix_random_h_1 = str("%02d" %jour) + '/' + str("%02d" %mois) + ' ' + str("%02d" %(int(cle[6:8])-1)) + cle[8:]
			nouveau_var = []
			for i in range(len(self.meteo[choix_random])):
				nouveau_var.append(str(float(self.meteo[cle][i])+float(self.meteo[choix_random][i])-float(self.meteo[choix_random_h_1][i])))
			for i in range(1, len(self.meteo[choix_random])):
				nouveau_var[i] = str(abs(float(nouveau_var[i])))
			self.meteo[cle] = tuple((nouveau_var))

	#Fonction permettant de renvoyer la liste avec tous les productions du site
	def init_production(self):
		#lecture du fichier
		#print "Liste production pas encore codé"
		PV1 = PV(0.18,1000,0.8) #http://www.capenergie.fr/catalogue/eolienne/eolienne-evance-r9000.html
		EO1 = EO(13,1000)
		return EO1,PV1

	#Fonction permettant de renvoyer la liste avec tous les stockages du site
	def init_liste_stockage(self):
		#lecture du fichier
		#print "Liste stockage pas encore codé"
		return []

	#Renvoie le nombre d'habitant du site
	def compteur_personne(self):

		nb_personne = 0
		for foyer in self.liste_foyer:
			nb_personne = nb_personne + len(foyer.liste_personne)			

		return nb_personne

	#Calcule de la consommation maximale moyenne sur une journée
	def consommation_moyenne_site(self):

		consommation_foyer_semaine = 0
		consommation_moyenne_jour = 0
		for foyer in self.liste_foyer:
				consommation_jt = 0
				consommation_jnt = 0
				for personne in foyer.liste_personne:
					for plage,tps_allumage in personne.tv_h_jt.items():
						consommation_jt += personne.tv.consommation_minute*tps_allumage
					for plage,tps_allumage in personne.pc_h_jnt.items():
						consommation_jnt += personne.pc.consommation_minute*tps_allumage

					for plage,tps_allumage in personne.pc_h_jt.items():
						consommation_jt += personne.pc.consommation_minute*tps_allumage
					for plage,tps_allumage in personne.pc_h_jnt.items():
						consommation_jnt += personne.pc.consommation_minute*tps_allumage

					for plage,tps_allumage in personne.pai_h_jt.items():
						consommation_jt += personne.pai.consommation_minute*tps_allumage
					for plage,tps_allumage in personne.pai_h_jnt.items():
						consommation_jnt += personne.pai.consommation_minute*tps_allumage	

					for plage,nb_allumage in personne.electro_h_jt.items():
						consommation_jt += personne.electro.consommation_minute*5*nb_allumage
					for plage,nb_allumage in personne.electro_h_jnt.items():
						consommation_jnt += personne.electro.consommation_minute*5*nb_allumage

				#Pour les lampes
				consommation_jt += consommation_jt*0.1
				consommation_jnt += consommation_jnt*0.1

				consommation_foyer_semaine = consommation_jt*5 + consommation_jnt*2
				consommation_foyer_semaine += foyer.nb_machine_a_laver*1000 + foyer.nb_lave_vaisselle*1000 + foyer.nb_seche_linge*1500
				#AJOUTER CHAUFFAGE CLIMATISATION FRIGO

				consommation_moyenne_jour += consommation_foyer_semaine / 7

		return consommation_moyenne_jour

	#Modifie les heures d'allumage et d'éteignage des appareils
	def actualisation_des_plages_h(self,minute,jour):		

		#Si on est entre lundi et vendredi et qu'on est sur une plage de mofication on calcul l'heure d'allumage et d'éteignage
		if(jour<5):
			for foyer in self.liste_foyer:
				for personne in foyer.liste_personne:
					#Gestion TV
					#Si la plage est dans la liste
					if(minute in personne.tv_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_tv_h = minute + randrange(0,361-personne.tv_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_tv_h = minute + randrange(0,181-personne.tv_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_tv_h = personne.allumage_tv_h + personne.tv_h_jt[minute] 

					if(minute in personne.pc_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pc_h = minute + randrange(0,361-personne.pc_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pc_h = minute + randrange(0,181-personne.pc_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pc_h = personne.allumage_pc_h + personne.pc_h_jt[minute]

					if(minute in personne.pai_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pai_h = minute + randrange(0,361-personne.pai_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pai_h = minute + randrange(0,181-personne.pai_h_jt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pai_h = personne.allumage_pai_h + personne.pai_h_jt[minute]

					if(minute in personne.electro_h_jt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.liste_allumage_h = sample(range(0,355),personne.electro_h_jt[minute]) 
						else:
							personne.liste_allumage_h = sample(range(0,175),personne.electro_h_jt[minute])
						for i in range(0,len(personne.liste_allumage_h)):
							personne.liste_allumage_h[i]+=minute
						personne.liste_eteignage_h = [temps+5 for temps in personne.liste_allumage_h]

		#Si on est samedi ou dimanche et qu'on est sur une plage de mofication on calcul l'heure d'allumage et d'éteignage
		elif(jour>=5):
			for foyer in self.liste_foyer:
				for personne in foyer.liste_personne:
					#Gestion TV
					#Si la plage est dans la liste
					if(minute in personne.tv_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_tv_h = minute + randrange(0,361-personne.tv_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_tv_h = minute + randrange(0,181-personne.tv_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_tv_h = personne.allumage_tv_h + personne.tv_h_jnt[minute] 

					if(minute in personne.pc_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pc_h = minute + randrange(0,361-personne.pc_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pc_h = minute + randrange(0,181-personne.pc_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pc_h = personne.allumage_pc_h + personne.pc_h_jnt[minute]

					if(minute in personne.pai_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.allumage_pai_h = minute + randrange(0,361-personne.pai_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						else:
							personne.allumage_pai_h = minute + randrange(0,181-personne.pai_h_jnt[minute]) #plage + rand(0,180-temps_allumage)
						personne.eteignage_pai_h = personne.allumage_pai_h + personne.pai_h_jnt[minute]

					if(minute in personne.electro_h_jnt):
						#Si on est entre 0h et 6h 
						if(minute<360):
							personne.liste_allumage_h = sample(range(0,355),personne.electro_h_jnt[minute]) 
						else:
							personne.liste_allumage_h = sample(range(0,175),personne.electro_h_jnt[minute])
						for i in range(0,len(personne.liste_allumage_h)):
							personne.liste_allumage_h[i]+=minute
						personne.liste_eteignage_h = [temps+5 for temps in personne.liste_allumage_h]
						
	#Allume ou éteint les appareils en fonction de l'heure de la journée
	def actualisation_des_foyers(self,minute,jour_semaine,nuit, cle):

		self.consommation_globale_minute = 0

		for foyer in self.liste_foyer:


				for minute_on_off,jour_allumage in foyer.heure_jour_on_off_machine_a_laver.items():
						if(jour_allumage == jour_semaine and minute_on_off[0] == minute and foyer.machine_a_laver.allume == False):
							foyer.machine_a_laver.allume = True
						if(jour_allumage == jour_semaine and minute_on_off[1] == minute and foyer.machine_a_laver.allume == True):
							foyer.machine_a_laver.allume = True

				for minute_on_off,jour_allumage in foyer.heure_jour_on_off_lave_vaisselle.items():
						if(jour_allumage == jour_semaine and minute_on_off[0] == minute and foyer.lave_vaisselle.allume == False):
							foyer.lave_vaisselle.allume = True
						if(jour_allumage == jour_semaine and minute_on_off[1] == minute and foyer.lave_vaisselle.allume == True):
							foyer.lave_vaisselle.allume = False

				for minute_on_off,jour_allumage in foyer.heure_jour_on_off_seche_linge.items():
						if(jour_allumage == jour_semaine and minute_on_off[0] == minute and foyer.seche_linge.allume == False):
							foyer.seche_linge.allume = True
						if(jour_allumage == jour_semaine and minute_on_off[1] == minute and foyer.seche_linge.allume == True):
							foyer.seche_linge.allume = False

				if(foyer.machine_a_laver.allume == True):
					self.consommation_globale_minute += foyer.machine_a_laver.consommation_minute
				if(foyer.lave_vaisselle.allume == True):
					self.consommation_globale_minute += foyer.lave_vaisselle.consommation_minute
				if(foyer.seche_linge.allume == True):
					self.consommation_globale_minute += foyer.seche_linge.consommation_minute

				if foyer.temperature<17.0 and foyer.chauffage==True:
					foyer.radiateur.allume=True
					temps_de_chauffe=((1.5*1.225*foyer.volume*1000*(22-foyer.temperature)/foyer.radiateur.consommation_heure))
					temps_de_chauffe=temps_de_chauffe/60
					self.variation_temp=(20-foyer.temperature)/temps_de_chauffe
					foyer.temperature+=self.variation_temp
					self.consommation_globale_minute+=foyer.radiateur.consommation_minute
				elif foyer.temperature<20.0 and foyer.radiateur.allume==True:
					foyer.temperature+=self.variation_temp
					self.consommation_globale_minute+=foyer.radiateur.consommation_minute
				else:
					foyer.radiateur.allume=False

				if foyer.temperature>25 and foyer.climatisation==True:
					foyer.clim.allume=True
					temps_de_chauffe=((1.5*1.225*foyer.volume*self.capa*(foyer.temperature-19)/foyer.clim.consommation_heure))
					temps_de_chauffe=temps_de_chauffe/60
					self.variation_temp=(22-foyer.temperature)/temps_de_chauffe
					foyer.temperature+=self.variation_temp
					self.consommation_globale_minute+=foyer.clim.consommation_minute
				elif foyer.temperature>22.0 and foyer.clim.allume==True:
					foyer.temperature+=self.variation_temp
					self.consommation_globale_minute+=foyer.clim.consommation_minute
				else:
					foyer.clim.allume=False				

				foyer.temperature = (60*((273+float(self.meteo[cle][0]))-(273+foyer.temperature))*self.lamb*foyer.surface_mur)/(foyer.epaisseur_mur*foyer.volume*self.capa) + foyer.temperature

				if foyer.frigo.temperature>5:
					foyer.frigo.allume=True
					temps_de_chauffe=((1.5*1.225*foyer.frigo.volume*10*self.capa*(2.0-foyer.frigo.temperature)/foyer.frigo.consommation_heure))
					temps_de_chauffe=temps_de_chauffe/60
					self.variation_temp_frigo=(foyer.frigo.temperature - 2.0)/temps_de_chauffe
					foyer.frigo.temperature+=self.variation_temp_frigo
					self.consommation_globale_minute+=foyer.frigo.consommation_minute
				elif foyer.frigo.temperature>2.0 and foyer.frigo.allume==True:
					foyer.frigo.temperature+=self.variation_temp_frigo
					self.consommation_globale_minute+=foyer.frigo.consommation_minute
				else:
					foyer.frigo.allume=False	

				foyer.frigo.temperature = (60*((273+foyer.temperature)-(273+foyer.frigo.temperature))*foyer.frigo.lamb*foyer.frigo.surface)/(foyer.frigo.epaisseur*foyer.frigo.volume*self.capa) + foyer.frigo.temperature

				for personne in foyer.liste_personne:

					#On considere tous les appareils éteints
					personne.lampe.allume = False

					#--------------- On regarde si on doit allumer ou éteindre les appareils ---------------#
					if(personne.allumage_tv_h == minute):
						personne.tv.allume = True
					elif(personne.eteignage_tv_h == minute):
						personne.tv.allume = False

					if(personne.allumage_pc_h == minute):
						personne.pc.allume = True
					elif(personne.eteignage_pc_h == minute):
						personne.pc.allume = False

					if(personne.allumage_pai_h == minute):
						personne.pai.allume = True
					elif(personne.eteignage_pai_h == minute):
						personne.pai.allume = False

					for minute_allumage in personne.liste_allumage_h:
						if(minute_allumage == minute):	
							personne.electro.allume = True
							personne.electro.nb_allumage = personne.electro.nb_allumage + 1

					for minute_eteignage in personne.liste_eteignage_h:
						if(minute_eteignage == minute):							
							personne.electro.nb_allumage = personne.electro.nb_allumage - 1
							if(personne.electro.nb_allumage == 0):
								personne.electro.allume = False

					#--------------- Calcule de la consommation globale ---------------#
					if(personne.tv.allume == True):
						if(nuit == True):
							personne.lampe.allume = True
						self.consommation_globale_minute += personne.tv.consommation_minute
					if(personne.pc.allume == True):
						if(nuit == True):
							personne.lampe.allume = True
						self.consommation_globale_minute += personne.pc.consommation_minute
					if(personne.pai.allume == True):
						if(nuit == True):
							personne.lampe.allume = True
						self.consommation_globale_minute += personne.pai.consommation_minute
					if(personne.electro.allume == True):
						if(nuit == True):
							personne.lampe.allume = True
						self.consommation_globale_minute += personne.electro.consommation_minute*personne.electro.nb_allumage
					if(personne.lampe.allume == True):
						self.consommation_globale_minute += personne.lampe.consommation_minute





	#Permet de modifier l'heure et jour d'allumage et éteignage des machines à laver, seche linge, lave vaisselle du foyer
	def actualisation_heure_jour_machine_foyer(self):

		for foyer in self.liste_foyer:
			
			i = 0
			while(i < foyer.nb_machine_a_laver):
				ok_allumage = True
				jour_tmp = randrange(0,7)
				minute_allumage_tmp = randrange(0,1260) #Heure d'allumage de minuit à 21h
				minute_eteignage_tmp = minute_allumage_tmp+randrange(30,180) #Heure éteignage entre 30min et 3h

				if(i == 0):
					foyer.heure_jour_on_off_machine_a_laver[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
					i+=1

				else:

					for minute_on_off,jour_allumage in foyer.heure_jour_on_off_machine_a_laver.items():
						if(jour_allumage == jour_tmp):
							if(minute_allumage_tmp > minute_on_off[0] and minute_eteignage_tmp < minute_on_off[1]):
								ok_allumage = False

					if(ok_allumage == True):
						foyer.heure_jour_on_off_machine_a_laver[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
						i+=1

			i = 0
			while(i < foyer.nb_lave_vaisselle):
				ok_allumage = True
				jour_tmp = randrange(0,7)
				minute_allumage_tmp = randrange(0,1260) #Heure d'allumage de minuit à 21h
				minute_eteignage_tmp = minute_allumage_tmp+randrange(30,180) #Heure éteignage entre 30min et 3h

				if(i == 0):
					foyer.heure_jour_on_off_lave_vaisselle[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
					i+=1

				else:

					for minute_on_off,jour_allumage in foyer.heure_jour_on_off_lave_vaisselle.items():
						if(jour_allumage == jour_tmp):
							if(minute_allumage_tmp > minute_on_off[0] and minute_eteignage_tmp < minute_on_off[1]):
								ok_allumage = False

					if(ok_allumage == True):
						foyer.heure_jour_on_off_lave_vaisselle[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
						i+=1

			i = 0
			while(i < foyer.nb_seche_linge):
				ok_allumage = True
				jour_tmp = randrange(0,7)
				minute_allumage_tmp = randrange(0,1260) #Heure d'allumage de minuit à 21h
				minute_eteignage_tmp = minute_allumage_tmp+randrange(30,180) #Heure éteignage entre 30min et 3h

				if(i == 0):
					foyer.heure_jour_on_off_seche_linge[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
					i+=1

				else:

					for minute_on_off,jour_allumage in foyer.heure_jour_on_off_seche_linge.items():
						if(jour_allumage == jour_tmp):
							if(minute_allumage_tmp > minute_on_off[0] and minute_eteignage_tmp < minute_on_off[1]):
								ok_allumage = False

					if(ok_allumage == True):
						foyer.heure_jour_on_off_seche_linge[(minute_allumage_tmp,minute_eteignage_tmp)] = jour_tmp
						i+=1
