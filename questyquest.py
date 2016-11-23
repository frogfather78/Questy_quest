
import pygame

from pygame.sprite import Group

from quester import Quester
from monster import Monster
from room import Room
from door import Door
from statsboard import Statsboard

import game_functions as gf


#let's play a game
pygame.init()
	
screen = pygame.display.set_mode((1080,800))
pygame.display.set_caption("Questy Quest")
game_active = True

#set up a quester	
bob = Quester(screen)
sb = Statsboard(screen,bob)

#create a room to be in
room = Room(screen)
door = Door(screen,room)

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
		gf.update_screen(screen,bob,monsters,room,door,sb)
		gf.check_quester_collision(screen,bob,monsters)


play_game()
