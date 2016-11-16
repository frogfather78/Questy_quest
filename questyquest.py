
import pygame

from pygame.sprite import Group

from quester import Quester
from monster import Monster
from room import Room

import game_functions as gf


#let's play a game
pygame.init()
	
screen = pygame.display.set_mode((1080,800))
pygame.display.set_caption("Questy Quest")
game_active = True

#set up a quester	
bob = Quester(screen)

#create a room to be in
room = Room(screen)

#do some stuff
bob.show_stats()


grue = Monster(screen, 2, room)

monsters = Group()

monsters.add(grue)
 
def play_game():
	"""main game loop"""
	while game_active:	
		
		gf.check_events(screen, bob, monsters)
		bob.update(room)
		#actually draw quester on screen
		gf.update_screen(screen,bob,monsters,room)
		gf.check_quester_collision(screen,bob,monsters)


play_game()
