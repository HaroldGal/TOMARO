#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class MoyenProduction:

	def __init__(self, en):
		self.id = -1
		self.energie=0

	def energieProduite(self):
		return energie

class Eolienne(MoyenProduction):
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+1

class Panneau(MoyenProduction):
	
	def __init(self, identite):
		self.id = i

	def production(self):
		self.energie= self.energie+2

if __name__=='__main__':
	p=Eolienne(1)
	for i in range(5):
		p.production()

	print(p.energie)
