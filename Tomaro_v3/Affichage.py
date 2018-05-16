#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pygame
import time
from pygame.locals import *
from random import randrange,sample,randint


#Fonction permettant de renvoyer les coordonnées pour centrer le texte au milieu d'une image
def centrer_texte(image,pos_x_image,pos_y_image,texte):
	return (pos_x_image+image.get_size()[0]/2-texte.get_size()[0]/2,pos_y_image+image.get_size()[1]/2-texte.get_size()[1]/2)

def menu(fenetre,nom_site,date,degre,vent,localisation,nb_foyer,nb_personne,consommation_totale,production_eo,production_pv,production_totale,stockage,stockage_pourcent,is_nuit,nb_eo,surface_pv,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche):	
	#S'il fait jour
	if(is_nuit==False):
		background = pygame.image.load("Image/Background_menu_jour.png").convert()
	else:
		background = pygame.image.load("Image/Background_menu_nuit.png").convert()
	fenetre.blit(background,(0,0))
	#Localisation
	font=pygame.font.Font(None, 30)
	localisation_str=font.render(localisation,1,(0,0,0))
	fenetre.blit(localisation_str,(630,40))

	#Soleil et lune	
	pas_temps=1000
	soleil = pygame.image.load("Image/Soleil.png").convert_alpha()
	lune = pygame.image.load("Image/Lune.png").convert_alpha()
	if is_nuit==False:
		for i in range(0,pas_temps):
			if minute_journee>=minute_leve+i*temps_jour/pas_temps and minute_journee<=minute_leve+(i+1)*temps_jour/pas_temps:
				if i<pas_temps/2:
					fenetre.blit(soleil,(1.2*i-100,250-0.5*i))
				else:
					fenetre.blit(soleil,(1.2*i-100,250-0.5*(pas_temps-1-i)))
				break

	elif is_nuit==True:
		for i in range(0,pas_temps):
			if minute_journee<minute_leve:
				minute_journee=minute_journee+1440
			if minute_journee>=minute_couche+i*temps_nuit/pas_temps and minute_journee<=minute_couche+(i+1)*temps_nuit/pas_temps:
				if i<pas_temps/2:
					fenetre.blit(lune,(1.2*i-50,300-0.6*i))
				else:
					fenetre.blit(lune,(1.2*i-50,300-0.6*(pas_temps-1-i)))
				break

	calque_batterie=pygame.image.load("Image/Bout_batterie.png").convert_alpha()
	fenetre.blit(calque_batterie,(942,463))
	
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
	font=pygame.font.Font(None, 15)
	nb_eo_str=font.render(nb_eo,1,(0,0,0))
	surface_pv_str=font.render(surface_pv,1,(0,0,0))
	font=pygame.font.Font(None, 40)
	production_totale_str=font.render(production_totale,1,(0,0,0))
	fenetre.blit(production_eo_str,(695-production_eo_str.get_size()[0],674))
	fenetre.blit(production_pv_str,(515-production_pv_str.get_size()[0],674))
	fenetre.blit(production_totale_str,(610-production_totale_str.get_size()[0],728))
	fenetre.blit(nb_eo_str,(764-nb_eo_str.get_size()[0]/2,695))
	fenetre.blit(surface_pv_str,(580-surface_pv_str.get_size()[0],694))

	#Stockage
	font=pygame.font.Font(None, 40)
	stockage_str=font.render(stockage,1,(0,0,0))
	font=pygame.font.Font(None, 30)
	stockage_pourcent_str=font.render(stockage_pourcent,1,(0,0,0))
	fenetre.blit(stockage_str,(1028-stockage_str.get_size()[0],707))
	fenetre.blit(stockage_pourcent_str,(1141-stockage_pourcent_str.get_size()[0]/2,750))


def affichage_liste_foyer(fenetre,site,date,is_nuit,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche):
	#S'il fait jour
	if(is_nuit==False):
		background = pygame.image.load("Image/Background_jour.png").convert()
	else:
		background = pygame.image.load("Image/Background_nuit.png").convert()
	liste_foyer_img=pygame.image.load("Image/Liste_foyer.png").convert_alpha()
	fenetre.blit(background,(0,0))
	#Soleil et lune	
	# pas_temps=1000
	# soleil = pygame.image.load("Image/Soleil.png").convert_alpha()
	# lune = pygame.image.load("Image/Lune.png").convert_alpha()
	# if is_nuit==False:
	# 	for i in range(0,pas_temps):
	# 		if minute_journee>=minute_leve+i*temps_jour/pas_temps and minute_journee<=minute_leve+(i+1)*temps_jour/pas_temps:
	# 			if i<pas_temps/2:
	# 				fenetre.blit(soleil,(1.2*i-100,350-0.5*i))
	# 			else:
	# 				fenetre.blit(soleil,(1.2*i-100,350-0.5*(pas_temps-1-i)))
	# 			break

	# elif is_nuit==True:
	# 	for i in range(0,pas_temps):
	# 		if minute_journee<minute_leve:
	# 			minute_journee=minute_journee+1440
	# 		if minute_journee>=minute_couche+i*temps_nuit/pas_temps and minute_journee<=minute_couche+(i+1)*temps_nuit/pas_temps:
	# 			if i<pas_temps/2:
	# 				fenetre.blit(lune,(1.2*i-50,400-0.6*i))
	# 			else:
	# 				fenetre.blit(lune,(1.2*i-50,400-0.6*(pas_temps-1-i)))
	# 			break
	fenetre.blit(liste_foyer_img,(10,10))

	#Date
	font=pygame.font.Font(None, 40)
	date=font.render(date,1,(0,0,0)) #Mettre date
	fenetre.blit(date,(1200-date.get_size()[0]-20,25))

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

def consommation_personne(personne):
	consommation=0
	if personne.tv.allume==True:
		consommation+=personne.tv.consommation_minute
	if personne.pc.allume==True:
		consommation+=personne.pc.consommation_minute
	if personne.pai.allume==True:
		consommation+=personne.pai.consommation_minute
	if personne.electro.allume==True:
		consommation+=personne.electro.consommation_minute*personne.electro.nb_allumage
	if personne.lampe.allume==True:
		consommation+=personne.lampe.consommation_minute

	return consommation

def consommation_foyer(foyer):
	consommation=0
	for personne in foyer.liste_personne:
		consommation+=consommation_personne(personne)
	if foyer.machine_a_laver.allume==True:
		consommation+=foyer.machine_a_laver.consommation_minute
	if foyer.seche_linge.allume==True:
		consommation+=foyer.seche_linge.consommation_minute
	if foyer.lave_vaisselle.allume==True:
		consommation+=foyer.lave_vaisselle.consommation_minute
	if foyer.frigo.allume==True:
		consommation+=foyer.frigo.consommation_minute
	if foyer.radiateur.allume==True:
		consommation+=foyer.radiateur.consommation_minute
	if foyer.climatisation.allume==True:
		consommation+=foyer.climatisation.consommation_minute

	return consommation



def affichage_foyer(fenetre,site,date,is_nuit,index_foyer,degre,temps_jour,temps_nuit,minute_journee,minute_leve,minute_couche,liste_objet):
	#S'il fait jour
	if(is_nuit==False):
		background = pygame.image.load("Image/Background_jour.png").convert()
	else:
		background = pygame.image.load("Image/Background_nuit.png").convert()
	foyer_img=pygame.image.load("Image/Foyer.png").convert_alpha()
	fenetre.blit(background,(0,0))
	#Soleil et lune	
	pas_temps=1000
	soleil = pygame.image.load("Image/Soleil.png").convert_alpha()
	lune = pygame.image.load("Image/Lune.png").convert_alpha()
	if is_nuit==False:
		for i in range(0,pas_temps):
			if minute_journee>=minute_leve+i*temps_jour/pas_temps and minute_journee<=minute_leve+(i+1)*temps_jour/pas_temps:
				if i<pas_temps/2:
					fenetre.blit(soleil,(1.2*i-100,250-0.5*i))
				else:
					fenetre.blit(soleil,(1.2*i-100,250-0.5*(pas_temps-1-i)))
				break

	elif is_nuit==True:
		for i in range(0,pas_temps):
			if minute_journee<minute_leve:
				minute_journee=minute_journee+1440
			if minute_journee>=minute_couche+i*temps_nuit/pas_temps and minute_journee<=minute_couche+(i+1)*temps_nuit/pas_temps:
				if i<pas_temps/2:
					fenetre.blit(lune,(1.2*i-50,300-0.6*i))
				else:
					fenetre.blit(lune,(1.2*i-50,300-0.6*(pas_temps-1-i)))
				break
	fenetre.blit(foyer_img,(0,11))

	#Date
	font=pygame.font.Font(None, 40)
	date=font.render(date,1,(0,0,0)) #Mettre date
	fenetre.blit(date,(1200-date.get_size()[0]-20,25))

	#Temperature
	font=pygame.font.Font(None, 40)
	temperature_ext=font.render(degre,1,(0,0,0))
	temperature_int=font.render(str(round(site.liste_foyer[index_foyer].temperature)),1,(0,0,0))
	fenetre.blit(temperature_ext,(1085-temperature_ext.get_size()[0],179))
	fenetre.blit(temperature_int,(595-temperature_int.get_size()[0],180))
	if site.liste_foyer[index_foyer].radiateur.allume==True:
		radiateur = pygame.image.load("Image/Radiateur_on.png").convert_alpha()
		fenetre.blit(radiateur,(772,189))
	elif site.liste_foyer[index_foyer].radiateur.allume==False:
		radiateur = pygame.image.load("Image/Radiateur_off.png").convert_alpha()
		fenetre.blit(radiateur,(772,189))

	if site.liste_foyer[index_foyer].climatisation.allume==True:
		climatisation = pygame.image.load("Image/Climatisation_on.png").convert_alpha()
		fenetre.blit(climatisation,(378,189))
	elif site.liste_foyer[index_foyer].climatisation.allume==False:
		climatisation = pygame.image.load("Image/Climatisation_off.png").convert_alpha()
		fenetre.blit(climatisation,(378,189))

	#Frigo/Electro Menagé
	nb_electro_allume=0
	pai_allume=False	
	nb_personne_cuisine=0
	cuisine_allume=False	

	#Chambre
	for index,personne in enumerate(site.liste_foyer[index_foyer].liste_personne):	
		#Personne 0
		if index==0:
			
			#Si nuit et lampe allumé	
			if personne.lampe.allume==True and is_nuit==True:
				lampe=pygame.image.load("Image/Lampe_on.png").convert_alpha()
				fenetre.blit(lampe,(374,283))

			#Si nuit et lampe éteinte
			elif personne.lampe.allume==False and is_nuit==True:
				chambre=pygame.image.load("Image/Chambre_1_sombre.png").convert_alpha()
				fenetre.blit(chambre,(322,282))
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(374,283))

			#Si c'est le jour lampe éteinte
			elif personne.lampe.allume==False and is_nuit==False:
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(374,283))

			#TV
			if personne.tv.allume==True:
				tv=pygame.image.load("Image/Tv_on.png").convert_alpha()
				fenetre.blit(tv,(432,297))
			elif personne.tv.allume==False:
				tv=pygame.image.load("Image/Tv_off.png").convert_alpha()
				fenetre.blit(tv,(432,297))
			#PC
			if personne.pc.allume==True:
				pc=pygame.image.load("Image/Pc_on.png").convert_alpha()
				fenetre.blit(pc,(524,300))
			elif personne.pc.allume==False:
				pc=pygame.image.load("Image/Pc_off.png").convert_alpha()
				fenetre.blit(pc,(524,300))

			#Affichage Personnage
			if consommation_personne(personne)==0 and is_nuit==False:
				pass
			elif consommation_personne(personne)==0 and is_nuit==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+"_couche_gauche.png").convert_alpha()
				fenetre.blit(perso,(349,323))
			elif personne.electro.nb_allumage>0 or personne.pai.allume==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680+nb_personne_cuisine*40,525))
				nb_personne_cuisine+=1
			else:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(490,305))
						

		#Personne 1
		if index==1:

			#Si nuit et lampe allumé	
			if personne.lampe.allume==True and is_nuit==True:
				lampe=pygame.image.load("Image/Lampe_on.png").convert_alpha()
				fenetre.blit(lampe,(780,283))

			#Si nuit et lampe éteinte
			elif personne.lampe.allume==False and is_nuit==True:
				chambre=pygame.image.load("Image/Chambre_2_sombre.png").convert_alpha()
				fenetre.blit(chambre,(604,282))
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(780,283))

			#Si c'est le jour lampe éteinte
			elif personne.lampe.allume==False and is_nuit==False:
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(780,283))

			#TV
			if personne.tv.allume==True:
				tv=pygame.image.load("Image/Tv_on.png").convert_alpha()
				fenetre.blit(tv,(710,297))
			elif personne.tv.allume==False:
				tv=pygame.image.load("Image/Tv_off.png").convert_alpha()
				fenetre.blit(tv,(710,297))

			#PC
			if personne.pc.allume==True:
				pc=pygame.image.load("Image/Pc_on.png").convert_alpha()
				fenetre.blit(pc,(618,298))
			elif personne.pc.allume==False:
				pc=pygame.image.load("Image/Pc_off.png").convert_alpha()
				fenetre.blit(pc,(618,298))

			#Affichage Personnage
			if consommation_personne(personne)==0 and is_nuit==False:
				pass
			elif consommation_personne(personne)==0 and is_nuit==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+"_couche_droite.png").convert_alpha()
				fenetre.blit(perso,(779,320))
			elif personne.electro.nb_allumage>0 or personne.pai.allume==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680+nb_personne_cuisine*40,525))
				nb_personne_cuisine+=1
			else:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680,305))

		#Personne 2
		if index==2:

			#Si nuit et lampe allumé	
			if personne.lampe.allume==True and is_nuit==True:
				lampe=pygame.image.load("Image/Lampe_on.png").convert_alpha()
				fenetre.blit(lampe,(374,399))

			#Si nuit et lampe éteinte
			elif personne.lampe.allume==False and is_nuit==True:
				chambre=pygame.image.load("Image/Chambre_3_sombre.png").convert_alpha()
				fenetre.blit(chambre,(322,398))
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(374,399))

			#Si c'est le jour lampe éteinte
			elif personne.lampe.allume==False and is_nuit==False:
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(374,399))

			#TV
			if personne.tv.allume==True:
				tv=pygame.image.load("Image/Tv_on.png").convert_alpha()
				fenetre.blit(tv,(432,412))
			elif personne.tv.allume==False:
				tv=pygame.image.load("Image/Tv_off.png").convert_alpha()
				fenetre.blit(tv,(432,412))

			#PC
			if personne.pc.allume==True:
				pc=pygame.image.load("Image/Pc_on.png").convert_alpha()
				fenetre.blit(pc,(524,410))
			elif personne.pc.allume==False:
				pc=pygame.image.load("Image/Pc_off.png").convert_alpha()
				fenetre.blit(pc,(524,410))

			#Affichage Personnage
			if consommation_personne(personne)==0 and is_nuit==False:
				pass
			elif consommation_personne(personne)==0 and is_nuit==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+"_couche_gauche.png").convert_alpha()
				fenetre.blit(perso,(349,431))
			elif personne.electro.nb_allumage>0 or personne.pai.allume==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680+nb_personne_cuisine*40,525))
				nb_personne_cuisine+=1

			else:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(490,415))

		#Personne 3
		if index==3:

			#Si nuit et lampe allumé	
			if personne.lampe.allume==True and is_nuit==True:
				lampe=pygame.image.load("Image/Lampe_on.png").convert_alpha()
				fenetre.blit(lampe,(780,399))

			#Si nuit et lampe éteinte
			elif personne.lampe.allume==False and is_nuit==True:
				chambre=pygame.image.load("Image/Chambre_4_sombre.png").convert_alpha()
				fenetre.blit(chambre,(604,398))
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(780,399))

			#Si c'est le jour lampe éteinte
			elif personne.lampe.allume==False and is_nuit==False:
				lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
				fenetre.blit(lampe,(780,399))

			#TV
			if personne.tv.allume==True:
				tv=pygame.image.load("Image/Tv_on.png").convert_alpha()
				fenetre.blit(tv,(710,412))
			elif personne.tv.allume==False:
				tv=pygame.image.load("Image/Tv_off.png").convert_alpha()
				fenetre.blit(tv,(710,412))

			#PC
			if personne.pc.allume==True:
				pc=pygame.image.load("Image/Pc_on.png").convert_alpha()
				fenetre.blit(pc,(618,410))
			elif personne.pc.allume==False:
				pc=pygame.image.load("Image/Pc_off.png").convert_alpha()
				fenetre.blit(pc,(618,410))

			#Affichage Personnage
			#Dans cuisine si un appareil est allumé ou pai
			if consommation_personne(personne)==0 and is_nuit==False:
				pass
			elif consommation_personne(personne)==0 and is_nuit==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+"_couche_droite.png").convert_alpha()
				fenetre.blit(perso,(779,426))
			elif personne.electro.nb_allumage>0 or personne.pai.allume==True:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680+nb_personne_cuisine*40,525))
			else:
				perso=pygame.image.load("Image/Personnage/Perso_"+str(personne.num_image)+".png").convert_alpha()
				fenetre.blit(perso,(680,415))

		#On regarde si la pai est allumé
		if personne.pai.allume==True:
			pai_allume=True

		#On regarde combien d'électro sont allumé
		nb_electro_allume+=personne.electro.nb_allumage

	if nb_electro_allume>0:
		cuisine_allume=True
	if pai_allume==True:
		cuisine_allume=True
		pai=pygame.image.load("Image/Pai_on.png").convert_alpha()

	else:
		pai=pygame.image.load("Image/Pai_off.png").convert_alpha()

	if cuisine_allume==False and is_nuit==True:
		cuisine_sombre=pygame.image.load("Image/Cuisine_sombre.png").convert_alpha()
		lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
		fenetre.blit(cuisine_sombre,(321,505))
		fenetre.blit(lampe,(393,506))
		fenetre.blit(lampe,(587,506))
		fenetre.blit(lampe,(778,506))

	elif cuisine_allume==True and is_nuit==True:
		lampe=pygame.image.load("Image/Lampe_on.png").convert_alpha()
		fenetre.blit(lampe,(393,506))
		fenetre.blit(lampe,(587,506))
		fenetre.blit(lampe,(778,506))
	else:
		lampe=pygame.image.load("Image/Lampe_off.png").convert_alpha()
		fenetre.blit(lampe,(393,506))
		fenetre.blit(lampe,(587,506))
		fenetre.blit(lampe,(778,506))

	if site.liste_foyer[index_foyer].frigo.allume==True:
		frigo = pygame.image.load("Image/Frigo_on.png").convert_alpha()
	elif site.liste_foyer[index_foyer].frigo.allume==False:		
		frigo = pygame.image.load("Image/Frigo_off.png").convert_alpha()	
	fenetre.blit(frigo,(325,510))
	fenetre.blit(pai,(627,562))

	#On affiche aléatoirement cafetiere,micro-onde,bouilloire ou grille-pain
	micro_onde_on=pygame.image.load("Image/Micro_onde_off.png").convert_alpha()
	fenetre.blit(micro_onde_on,(395,541))
	bouilloire_on=pygame.image.load("Image/Bouilloire_off.png").convert_alpha()
	fenetre.blit(bouilloire_on,(600,548))
	cafetiere_on=pygame.image.load("Image/Cafetiere_off.png").convert_alpha()
	fenetre.blit(cafetiere_on,(471,537))
	grille_pain_on=pygame.image.load("Image/Grille_pain_off.png").convert_alpha()
	fenetre.blit(grille_pain_on,(518,544))

	liste_electro_allume=sample(range(0,4),4)

	for i in range(0,nb_electro_allume):
		if i==liste_electro_allume[0]:
			micro_onde_on=pygame.image.load("Image/Micro_onde_on.png").convert_alpha()
			fenetre.blit(micro_onde_on,(395,541))
		elif i==liste_electro_allume[1]:
			bouilloire_on=pygame.image.load("Image/Bouilloire_on.png").convert_alpha()
			fenetre.blit(bouilloire_on,(600,548))
		elif i==liste_electro_allume[2]:
			cafetiere_on=pygame.image.load("Image/Cafetiere_on.png").convert_alpha()
			fenetre.blit(cafetiere_on,(471,537))
		elif i==liste_electro_allume[3]:
			grille_pain_on=pygame.image.load("Image/Grille_pain_on.png").convert_alpha()
			fenetre.blit(grille_pain_on,(518,544))	

	#Garage
	if is_nuit==True and site.liste_foyer[index_foyer].machine_a_laver.allume==False and site.liste_foyer[index_foyer].seche_linge.allume==False and site.liste_foyer[index_foyer].lave_vaisselle.allume==False:
		background_cave_sombre=pygame.image.load("Image/Background_cave_sombre.png").convert_alpha()
		fenetre.blit(background_cave_sombre,(321,619))
	if site.liste_foyer[index_foyer].machine_a_laver.allume==True:
		machine_a_laver=pygame.image.load("Image/Machine_a_laver_on.png").convert_alpha()
		fenetre.blit(machine_a_laver,(436,647))
	else:
		machine_a_laver=pygame.image.load("Image/Machine_a_laver_off.png").convert_alpha()
		fenetre.blit(machine_a_laver,(416,647))

	if site.liste_foyer[index_foyer].seche_linge.allume==True:
		seche_linge=pygame.image.load("Image/Seche_linge_on.png").convert_alpha()
	else:
		seche_linge=pygame.image.load("Image/Seche_linge_off.png").convert_alpha()

	if site.liste_foyer[index_foyer].lave_vaisselle.allume==True:
		lave_vaisselle=pygame.image.load("Image/Lave_vaisselle_on.png").convert_alpha()
	else:
		lave_vaisselle=pygame.image.load("Image/Lave_vaisselle_off.png").convert_alpha()

	
	fenetre.blit(lave_vaisselle,(584,647))
	fenetre.blit(seche_linge,(732,647))
	


	#On affiche les chambres vides
	if site.liste_foyer[index_foyer].nombre_individu==1:
		chambre_vide=pygame.image.load("Image/Chambre_2_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(604,282))
		chambre_vide=pygame.image.load("Image/Chambre_3_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(322,398))
		chambre_vide=pygame.image.load("Image/Chambre_4_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(604,398))

	elif site.liste_foyer[index_foyer].nombre_individu==2:
		chambre_vide=pygame.image.load("Image/Chambre_3_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(322,398))
		chambre_vide=pygame.image.load("Image/Chambre_4_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(604,398))

	elif site.liste_foyer[index_foyer].nombre_individu==3:
		chambre_vide=pygame.image.load("Image/Chambre_4_vide.png").convert_alpha()
		fenetre.blit(chambre_vide,(604,398))

	#Affichage des part de consommation dans la maison
	if len(liste_objet)!=0:
		font=pygame.font.Font(None,35)
		titre=font.render("Part de consommation:",1,(0,0,0))
		fenetre.blit(titre,(20,350))

	font=pygame.font.Font(None,30)	
	for index1,personne in enumerate(site.liste_foyer[index_foyer].liste_personne):
		for index_objet,objet in enumerate(liste_objet):
			if index1==objet[1] and consommation_foyer(site.liste_foyer[index_foyer])!=0:
				if objet[0]=="lampe":
					if personne.lampe.allume==True:
						conso_str=font.render(personne.lampe.nom+" chambre "+str(objet[1]+1)+" - "+str(round(personne.lampe.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif personne.lampe.allume==False:
						conso_str=font.render(personne.lampe.nom+" chambre "+str(objet[1]+1)+" - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="tv":
					if personne.tv.allume==True:
						conso_str=font.render(personne.tv.nom+" chambre "+str(objet[1]+1)+" - "+str(round(personne.tv.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif personne.tv.allume==False:
						conso_str=font.render(personne.tv.nom+" chambre "+str(objet[1]+1)+" - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="pc":
					if personne.pc.allume==True:
						conso_str=font.render(personne.pc.nom+" chambre "+str(objet[1]+1)+" - "+str(round(personne.pc.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif personne.pc.allume==False:
						conso_str=font.render(personne.pc.nom+" chambre "+str(objet[1]+1)+" - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="pai":
					consommation_pai=0
					for personne in site.liste_foyer[index_foyer].liste_personne:
						if personne.pai.allume==True:
							consommation_pai+=personne.pai.consommation_minute
					conso_str=font.render("Plaques induction - "+str(round(consommation_pai*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
					fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="frigo":
					if site.liste_foyer[index_foyer].frigo.allume==True:
						conso_str=font.render("Frigo - "+str(round(site.liste_foyer[index_foyer].frigo.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].frigo.allume==False:
						conso_str=font.render("Frigo - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="electro":
					consommation_electro=0
					for personne in site.liste_foyer[index_foyer].liste_personne:
						if personne.electro.allume==True:
							consommation_electro+=personne.electro.consommation_minute*personne.electro.nb_allumage
					conso_str=font.render("Electromenages - "+str(round(consommation_electro*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
					fenetre.blit(conso_str,(20,400+index_objet*30))
					
				if objet[0]=="radiateur":
					if site.liste_foyer[index_foyer].radiateur.allume==True:
						conso_str=font.render("Chauffage - "+str(round(site.liste_foyer[index_foyer].radiateur.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].radiateur.allume==False:
						conso_str=font.render("Chauffage - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="climatisation":
					if site.liste_foyer[index_foyer].climatisation.allume==True:
						conso_str=font.render("Climatisation - "+str(round(site.liste_foyer[index_foyer].climatisation.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].climatisation.allume==False:
						conso_str=font.render("Climatisation - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="machine_a_laver":
					if site.liste_foyer[index_foyer].machine_a_laver.allume==True:
						conso_str=font.render("Machine a laver - "+str(round(site.liste_foyer[index_foyer].machine_a_laver.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].machine_a_laver.allume==False:
						conso_str=font.render("Machine a laver - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="seche_linge":
					if site.liste_foyer[index_foyer].seche_linge.allume==True:
						conso_str=font.render("Seche linge - "+str(round(site.liste_foyer[index_foyer].seche_linge.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].seche_linge.allume==False:
						conso_str=font.render("Seche linge - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))

				if objet[0]=="lave_vaisselle":
					if site.liste_foyer[index_foyer].lave_vaisselle.allume==True:
						conso_str=font.render("Lave vaisselle - "+str(round(site.liste_foyer[index_foyer].lave_vaisselle.consommation_minute*100/consommation_foyer(site.liste_foyer[index_foyer])))+" %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))
					elif site.liste_foyer[index_foyer].lave_vaisselle.allume==False:
						conso_str=font.render("Lave vaisselle - 0.0 %",1,(0,0,0))
						fenetre.blit(conso_str,(20,400+index_objet*30))