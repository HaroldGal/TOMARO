#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from time import sleep
import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab


fig = pylab.figure(figsize=[6, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
matplotlib.pyplot.title("Courbe de charge")
matplotlib.pyplot.ion()


data = []
axe_temps = []
ax.set_xticklabels(axe_temps)
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

import pygame
from pygame.locals import *



def courbe_maj(val,temps):
	# sleep(1)
	pygame.init()

	window = pygame.display.set_mode((600, 400), DOUBLEBUF)
	screen = pygame.display.get_surface()

	size = canvas.get_width_height()

	cmap = matplotlib.pyplot.get_cmap('jet_r')
	color = cmap(float(1)/256)
	
	if len(data)<72: # Il faut changer afin que = 24*60/pas_de_temps
		data.append(val)
		
	else :
		ax.cla()
		data.pop(0)
		axe_temps.pop(0)
		data.append(val)
	if temps%180 == 0:
		axe_temps.append(str(temps/60)+"h")
	else :
		axe_temps.append('')
	ax.plot(range(len(data)), data, c=color)
	ax.set_xticks(range(len(data)))
	ax.set_xticklabels(axe_temps)

	canvas.draw()
	raw_data = renderer.tostring_rgb()
	surf = pygame.image.fromstring(raw_data, size, "RGB")
	screen.blit(surf, (0,0))
	pygame.display.flip()

