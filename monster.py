import dice as d
import pygame

from random import randint
from pygame.sprite import Sprite

class Monster(Sprite):
	"""something a quester might fight or whatever"""
	def __init__(self, screen, level, room):
		
		super(Monster,self).__init__()
		
		self.screen = screen
		
		#initialise some things about quester
		self.hp = (20 * level) + 4 * d.roll(6)
		self.max_hp = self.hp 
		self.strength = (3 * level) + d.roll(6)
		self.magic = (3 * level) + d.roll(6)
			
		self.level = level
		
		#load image and get rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#place monster somewhere in room??
		self.x = randint(room.rect.left, room.rect.right)
		self.rect.centerx = self.x
		self.y = randint(room.rect.top, room.rect.bottom)
		self.rect.centery = self.y

	def show_stats(self):
		"""display information about monster"""
		print("HP: " + str(self.hp)+"/"+ str(self.max_hp))
		print("Level: " + str(self.level))
		print("s: " + str(self.strength) + " m: " + str(self.magic))

	def blitme(self):
		"""draw monster at current location"""
		self.screen.blit(self.image, self.rect)
