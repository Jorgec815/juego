import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/barril.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[0])
		self.velocidad=vel
        
	def update(self, heroe):
		if heroe.vida > 0:
			self.rect.x -= self.velocidad
			teclas = pygame.key.get_pressed()
			if teclas[K_a] and self.velocidad > 1:
				self.velocidad = self.velocidad-1 
			elif teclas[K_d] and self.velocidad < 10:
				self.velocidad = self.velocidad+1
		
