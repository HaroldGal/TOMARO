from mpi4py import MPI
from Site import *
import time

site_alpha = Site("Campus",100)
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
#minute_journee = plage_proche(now.tm_hour*60+now.tm_min,plage) #Commence une minute avant un plage existante
site_alpha.actualisation_heure_jour_machine_foyer()
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = site_alpha.liste_foyer
    for i in range(1,size):
    	print i
    	comm.send(data[(i)*len(data)/size:(i+1)*len(data)/size], dest=i, tag=11)
else:
    data=comm.recv(source=0, tag=11)


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

				if foyer.temperature<20.0 and foyer.chauffage==True:
					temps_de_chauffe=((1.5*1.225*foyer.volume*1000*(20-foyer.temperature)/foyer.radiateur.consommation_heure))
					temps_de_chauffe=temps_de_chauffe/60
					augmentation_temp=(20-foyer.temperature)/temps_de_chauffe
					foyer.temperature+=augmentation_temp
					self.consommation_globale_minute+=foyer.radiateur.consommation_minute
				foyer.temperature = (60*((273+float(self.meteo[cle][0]))-(273+foyer.temperature))*self.lamb*foyer.surface_mur)/(foyer.epaisseur_mur*foyer.volume*self.capa) + foyer.temperature


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




