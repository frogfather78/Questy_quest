
import pygame

from pygame.sprite import Group

from quester import Quester
from monster import Monster
from qqmap import Qqmap
from room import Room
from room import Door
from statsboard import Statsboard

import game_functions as gf


#let's play a game
pygame.init()
	
screen = pygame.display.set_mode((1080,800))
pygame.display.set_caption("Questy Quest")
game_active = True


floor = Qqmap(screen)
location = floor.start

#create a room to be in, put it in a group
room = Room(floor, location, screen)
#open_rooms = Group()
floor.open_rooms.add(room)

#set up a quester	
bob = Quester(screen,location)
sb = Statsboard(screen,bob)

#do some stuff
bob.show_stats()


grue = Monster(screen, 2, room)
brue = Monster(screen, 2, room)

monsters = Group()

monsters.add(grue)
monsters.add(brue)
 
def play_game():
	"""main game loop"""
	while game_active:	
		
		gf.check_events(screen, bob, monsters)
		bob.update(room)
		#actually draw quester on screen
		sb.prep_stats(bob)
		gf.update_screen(screen,bob,monsters,floor,sb)
		gf.check_quester_collision(screen,bob,monsters,room.doors, 
			floor)


play_game()
