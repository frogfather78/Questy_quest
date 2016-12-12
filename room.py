from pygame.sprite import Sprite
from pygame.sprite import Group

import random

import pygame
import qqmap



class Room(Sprite):
	"""a room in which one might walk around"""
		
	def __init__(self,qqmap,location,screen,side=''):
		"""some things about the room"""
		super(Room,self).__init__()
		
		self.bg_colour = (40,40,40)
		self.width = 500
		self.height = 400
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.screen = screen
		self.map = qqmap
		
		self.screen_rect = screen.get_rect()
		
		#place room in centre of screen if it's the first room
		if len(self.map.open_rooms) == 0:
			self.rect.centerx = self.screen_rect.centerx
			self.rect.centery = self.screen_rect.centery
		#location is its index in the floorplan
		self.location = location
		
		if side == 'w':
			self.rect.centerx = self.screen_rect.centerx - (self.width + 5)
			self.rect.centery = self.screen_rect.centery
		
		
		self.map_width = self.map.floorplan[0]
		
		self.find_doors()
		
		
	def find_doors(self):
		self.doors = Group()
		print(str(self.location % self.map_width))
		
		if self.location-self.map_width > 1:
			if self.map.floorplan[self.location-self.map_width]:
				door = Door(self.screen, self, "n")
				self.doors.add(door)
				#door to the north
			
		if self.location+1 < len(self.map.floorplan):
			if (self.map.floorplan[self.location+1] and
				self.location % self.map_width != 0):
					door = Door(self.screen, self, "e")
					self.doors.add(door) #door to the east
				
		if self.location+self.map_width < len(self.map.floorplan):
			if self.map.floorplan[self.location+self.map_width]:
				door = Door(self.screen, self, "s")
				self.doors.add(door) #door to the south
		
		if (self.map.floorplan[self.location-1] and
			(self.location-1) % self.map_width != 0):
				door = Door(self.screen, self, "w")
				self.doors.add(door)#door to the west
			
		
	def draw_room(self):
		"""draw room to screen"""
		pygame.draw.rect(self.screen, self.bg_colour, self.rect)
		
	
class Door(Sprite):
	"""a door through which one might leave a room"""
		
	def __init__(self,screen,room,side):
		"""some things about the door"""
		super(Door,self).__init__()
		
		#load image and get rect
		self.image = pygame.image.load('images/door.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.side = side
		
		self.screen = screen
		
		#figure out where to add doors
		
		if side == "n":
			self.rect.centerx = room.rect.left + room.width/2
			self.rect.centery = room.rect.top
		elif side == "e":
			self.rect.centery = room.rect.top + room.height/2
			self.rect.centerx = room.rect.right
		elif side == "w":
			self.rect.centery = room.rect.top + room.height/2
			self.rect.centerx = room.rect.left
		elif side == "s":
			self.rect.centerx = room.rect.left + room.width/2
			self.rect.centery = room.rect.bottom

	def blitme(self):
		"""draw to screen"""
		self.screen.blit(self.image, self.rect)
