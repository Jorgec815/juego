import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/barril.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[0])
		self.velocidad=vel
        
	def update(self):
		self.rect.y += self.velocidad 
		self.rect.y = self.rect.y % 640
