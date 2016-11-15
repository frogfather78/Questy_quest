import dice as d
import pygame

from pygame.sprite import Sprite

class Monster(Sprite):
	"""something a quester might fight or whatever"""
	def __init__(self, screen, level):
		
		super(Monster,self).__init__()
		
		self.screen = screen
		
		#initialise some things about quester
		self.hp = (20 * level) + 4 * d.roll(6)
		self.max_hp = self.hp 
		self.strength = (5 * level) + d.roll(6)
		self.magic = (3 * level) + d.roll(6)
			
		self.level = level
		
		#load image and get rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#place quester in centre of screen
		self.rect.centerx = self.screen_rect.centerx + 50
		self.rect.centery = self.screen_rect.centery - 50

	def show_stats(self):
		"""display information about monster"""
		print("HP: " + str(self.hp)+"/"+ str(self.max_hp))
		print("Level: " + str(self.level))
		print("s: " + str(self.strength) + " m: " + str(self.magic))

	def blitme(self):
		"""draw monster at current location"""
		self.screen.blit(self.image, self.rect)
