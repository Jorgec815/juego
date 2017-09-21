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
        
	def update(self):
		self.rect.x -= self.velocidad 
		self.rect.x = self.rect.x % 640
		teclas = pygame.key.get_pressed()
		if teclas[K_LEFT] and self.velocidad > 1:
			self.velocidad = self.velocidad-1 
		elif teclas[K_RIGHT] and self.velocidad < 15:
			self.velocidad = self.velocidad+1
