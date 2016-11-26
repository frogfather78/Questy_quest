
from room import Room

from pygame.sprite import Group

class Map():
	"""around which one can navigate"""
	
	def __init__(screen):
		self.floor_plan = [4,
			0, 0, 3, 0,
			2, 2, 2, 0,
			1, 2, 2, 2]
		
		#1 = first room
		#2 = any other room
		#3 = last room
		#first entry = width of array

		self.rooms = Group()
		
		start = self.floor_plan.index(1)
		self.first_room = Room(screen, start) #???
		#make a room that corresponds to the place in the floor plan
		#where the number 1 appears
		#but what does this MEAN?
		
		self.rooms.add(self.first_room)
