import sys

import pygame

from quester import Quester
from monster import Monster
from room import Room
import dice as d

from time import sleep

def check_keydown_events(event,screen,quester):
	"""respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		#move quester to the right
		quester.moving_right = True
	elif event.key == pygame.K_LEFT:
		#move quester to the left
		quester.moving_left = True

	elif event.key == pygame.K_UP:
		#move quester up
		quester.moving_up = True
	elif event.key == pygame.K_DOWN:
		#move quester down
		quester.moving_down = True	

	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,screen,quester):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		#move quester to the right
		quester.moving_right = False
	elif event.key == pygame.K_LEFT:
		#move quester to the left
		quester.moving_left = False

	elif event.key == pygame.K_UP:
		#move quester up
		quester.moving_up = False
	elif event.key == pygame.K_DOWN:
		#move quester down
		quester.moving_down = False	


def check_events(screen,quester,monsters):
	"""respond to keypresses and mouses"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,screen,quester)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,screen,quester)

def check_quester_collision(screen,quester,monsters,doors,floor):
	"""check to see if quester has bumped into anything
	 and interact with it"""
	#dokill = false because we don't want to kill unless quester wins 
	combatants = pygame.sprite.spritecollide(quester,monsters,False)
	for monster in combatants:
		fight(quester,monster)
	open_doors = pygame.sprite.spritecollide(quester,doors,True)
	#remove door because we'll just put in a new room
	
	for open_door in open_doors:
		new_loc = quester.location
		print("open a door " + open_door.side)
		if open_door.side == "w":
			new_loc = quester.location - 1
		open_room(screen,quester,new_loc,floor,open_door.side)
		
def open_room(screen,quester,new_loc,floor,side):
	"""open a door to a new room"""
	new_room = Room(floor,new_loc,screen,side)
	floor.open_rooms.add(new_room)
	print(str(floor.open_rooms))


def update_screen(screen, quester, monsters, floor, sb):
	"""update images on screen and flip to new screen"""
	#redraw stuff behind quester and monster(s)
	bg_colour = (10,10,10)
	screen.fill(bg_colour)
	
	#draw room on top of absolute background
	for room in floor.open_rooms:
		room.draw_room()
		room.doors.draw(screen)
	
	quester.blitme()
	monsters.draw(screen)
	sb.show_stats()

	#make most recently drawn screen visible
	pygame.display.flip()


def fight(quester, monster):
	"""just battering each other, basically"""
	sleep(0.5) #just pause for a beat before doing the fighting
	while quester.hp > 0:
		if (d.roll(10) * quester.strength) > (d.roll(10) * monster.strength):
			#quester hits monster
			monster.hp -= quester.strength
			print("Quester hits monster")
			if monster.hp <= 0:
				#monster dies, quester wins
				print("Quester beats monster!")
				quester.gain_xp(monster.level * d.roll(4))
				monster.kill()
				break
		else:
			#monster hits quester
			quester.hp -= monster.strength
			print("Monster hits quester")
			if quester.hp <= 0:
				#quester dies. oh noes
				print("Quester dies!")
				break










