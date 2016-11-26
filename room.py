from pygame.sprite import Sprite

import pygame

class Room(Sprite):
	"""a room in which one might walk around"""
		
	def __init__(self,screen,location):
		"""some things about the room"""
		super(Room,self).__init__()
		
		self.bg_colour = (40,40,40)
		self.width = 500
		self.height = 400
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.screen = screen
		#place room in centre of screen
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		#location is its index in the floor_plan
		self.location = location 
		
	def draw_room(self):
		"""draw room to screen"""
		pygame.draw.rect(self.screen, self.bg_colour, self.rect)
		
	
