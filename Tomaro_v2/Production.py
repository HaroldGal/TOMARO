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
		return self.rendement*self.surface*self.Cp*radiation_global+randrange(0,3)*0.05*self.rendement*self.surface*self.Cp*radiation_global

class EO(Production):

	def __init__(self, surface_pale, nb):

		Production.__init__(self)
		self.surface_pale = surface_pale
		self.nb = nb

	def production_energie(self,vitesse_vent):

		self.production_energie_jour += self.nb*self.surface_pale*0.5*1.2*vitesse_vent
		return self.nb*self.surface_pale*0.5*1.2*vitesse_vent+randrange(0,3)*0.05*self.nb*self.surface_pale*0.5*1.2*vitesse_vent