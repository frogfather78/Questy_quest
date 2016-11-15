import sys

import pygame

from quester import Quester
from monster import Monster
import dice as d



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

def check_quester_collision(screen,quester,monsters):
	"""check to see if quester has bumped into anything and fight it"""
	#dokill = false because we don't want to kill unless quester wins 
	combatants = pygame.sprite.spritecollide(quester,monsters,False)
	for monster in combatants:
		fight(quester,monster)


def update_screen(screen, quester, monsters):
	"""update images on screen and flip to new screen"""
	#redraw stuff behind quester and monster(s)
	bg_colour = (90,90,90)
	screen.fill(bg_colour)
	
	quester.blitme()
	monsters.draw(screen)


	#make most recently drawn screen visible
	pygame.display.flip()


def fight(quester, monster):
	"""just battering each other, basically"""
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










