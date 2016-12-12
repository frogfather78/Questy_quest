
from room import Room

from pygame.sprite import Group

class Qqmap():
	"""around which one can navigate"""
	
	def __init__(self,screen):
		self.floorplan = [4,
			0, 0, 3, 0,
			2, 2, 2, 0,
			2, 2, 2, 1]
		
		#1 = first room
		#2 = any other room
		#3 = last room
		#first entry = width of array
		
		self.start = self.floorplan.index(1)
		self.open_rooms = Group()
		
		
