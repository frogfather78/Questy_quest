import dice as d
import pygame

from monster import Monster

from pygame.sprite import Sprite

level_limits = [0, 10, 100, 300, 600, 1000, 1500, 2500]

class Quester(Sprite):
	"""someone who goes on a questy quest"""
	def __init__(self,screen):
		#initialise some things about quester
		super(Quester,self).__init__()
		
		self.screen = screen
		
		#load image and get rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#place quester in centre of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		#start off stationary
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		
		#stats about the quester
		self.xp = 0
		self.hp = 100 + 10 * d.roll(6)
		self.max_hp = self.hp
		self.strength = 10 + d.roll(6)
		self.magic = 10 + d.roll(6)
		
		self.level = 1
		
	def show_stats(self):
		"""display information about quester"""
		print("HP: " + str(self.hp)+"/"+ str(self.max_hp))
		print("XP: " + str(self.xp)+"/"+ 
			str(level_limits[self.level]))
		print("Level: " + str(self.level))
		print("s: " + str(self.strength) + " m: " + str(self.magic))
		
	def gain_xp(self, points):
		"""when quester does something good"""
		self.xp += points
		#check if this takes quester into a new level
		if self.xp > level_limits[self.level]:
			#level up
			print("Level Up!")
			self.level_up()

	def level_up(self):
		"""increase stats and that"""
		self.level += 1
		self.max_hp = int(self.max_hp * 1.5)
		#full healing!
		self.hp = self.max_hp
		self.strength = int(self.strength * 1.5)
		self.magic = int(self.magic * 1.5)

	def update(self):
		"""update position based on movement flag"""
		#move up/down/let/right within screen
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 5
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 5
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 5
		if self.moving_up and self.rect.top > 0:
			self.rect.centery -= 5


	def blitme(self):
		"""draw quester at current location"""
		self.screen.blit(self.image, self.rect)
