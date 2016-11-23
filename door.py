from pygame.sprite import Sprite

import pygame
import random

class Door(Sprite):
	"""a door through which one might leave a room"""
		
	def __init__(self,screen,room):
		"""some things about the room"""
		super(Door,self).__init__()
		
		#load image and get rect
		self.image = pygame.image.load('images/door.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		self.screen = screen
		
		#pick a side of the room
		self.side = random.choice(['top','left','right'])
		if self.side == 'top':
			self.rect.centerx = room.rect.left + room.width/2
			self.rect.centery = room.rect.top
		elif self.side == 'left':
			self.rect.centery = room.rect.top + room.height/2
			self.rect.centerx = room.rect.left
		elif self.side == 'right':
			self.rect.centery = room.rect.top + room.height/2
			self.rect.centerx = room.rect.right

	def draw_door(self):
		"""draw to screen"""
		self.screen.blit(self.image, self.rect)
