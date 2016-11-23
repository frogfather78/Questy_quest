import pygame.font
from pygame.sprite import Group

from quester import Quester

level_limits = [0, 10, 100, 300]

class Statsboard():
	"""to show quester's stats"""
	
	def __init__(self, screen, quester):
		"""set up some things for the board"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#font settings for scoring information
		self.text_colour = (255, 255, 255)
		self.bg_colour = (0,0,0)
		self.font = pygame.font.SysFont(None, 20)
		
		self.prep_stats(quester)
		
	def prep_stats(self,quester):
		"""set up stats as a renderable image"""
		
		#create strings for stats
		hp_str = ("HP: " + str(quester.hp)+"/"+ str(quester.max_hp))
		xp_str = ("XP: " + str(quester.xp)+"/"+ 
			str(level_limits[quester.level]))
		level_str = ("Level: " + str(quester.level))
		stats_str = ("s: " + str(quester.strength) + 
			" m: " + str(quester.magic))

		#render images
		self.hp_image = self.font.render(hp_str, True, 
			self.text_colour, self.bg_colour)
		self.xp_image = self.font.render(xp_str, True, 
			self.text_colour, self.bg_colour)
		self.level_image = self.font.render(level_str, True, 
			self.text_colour, self.bg_colour)
		self.stats_image = self.font.render(stats_str, True, 
			self.text_colour, self.bg_colour)

		#put the images to the top left of the screen
		self.hp_rect = self.hp_image.get_rect()
		self.xp_rect = self.xp_image.get_rect()
		self.level_rect = self.level_image.get_rect()
		self.stats_rect = self.stats_image.get_rect()
		
		self.hp_rect.left = self.screen_rect.left + 5
		self.hp_rect.top = 20
		self.xp_rect.left = self.screen_rect.left + 5
		self.xp_rect.top = 35
		self.level_rect.left = self.screen_rect.left + 5
		self.level_rect.top = 50
		self.stats_rect.left = self.screen_rect.left + 5
		self.stats_rect.top = 65

	def show_stats(self):
		"""draw the stats onto the screen"""
		self.screen.blit(self.hp_image, self.hp_rect)
		self.screen.blit(self.xp_image, self.xp_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.stats_image, self.stats_rect)
