#!/usr/bin/python2.7	
#-*- coding: utf-8 -*-

from random import randrange

class Production:

	def __init__(self):

		self.production_energie_jour = 0 #En W.h

class PV(Production):

	def __init__(self,rendement,surface,Cp):

		Production.__init__(self)
		self.rendement = rendement
		self.surface = surface
		self.Cp = Cp

	def production_energie(self,radiation_global):

		self.production_energie_jour += self.rendement*self.surface*self.Cp*radiation_global
		return self.rendement*self.surface*self.Cp*radiation_global+randrange(-3,3)*0.05*self.rendement*self.surface*self.Cp*radiation_global

class EO(Production):

	def __init__(self, surface_pale, nb, performance):

		Production.__init__(self)
		self.surface_pale = surface_pale
		self.nb = nb
		self.performance = performance

	def production_energie(self,vitesse_vent):

		#https://heliciel.com/helice/eolienne%20hydrolienne/energie-eolienne.htm
		#https://eolienne.ooreka.fr/astuce/voir/352953/puissance-eolienne
		#Pour produire de l'énergie le vent doit avoir une vitesse minimum de 3m/s
		if vitesse_vent>3:
				self.production_energie_jour += self.nb*self.surface_pale*0.5*1.2*(vitesse_vent)**3*self.performance
				return self.nb*self.surface_pale*0.5*1.2*(vitesse_vent)**3*self.performance+randrange(-3,3)*0.05*self.nb*self.surface_pale*0.5*1.2*(vitesse_vent)**3*self.performance
		return 0
		