import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.estado = "derecha"
		self.imagenes = [util.cargar_imagen('imagenes/personaje1.png'),
						util.cargar_imagen('imagenes/personaje2.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(10, 240)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[0]
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]
		else:
			self.image = self.imagenes[0]
