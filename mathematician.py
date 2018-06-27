from random import randint
import json
import random

from mission import mission


#load plot and level up text into p_data
f_name = "math_plot.json"


def load_plot_data(f_name):

	try:
		with open(f_name) as f_obj:
			plot_data = json.load(f_obj)
		
	except FileNotFoundError:
		return None
	else:
		return plot_data

p_data = load_plot_data(f_name)

# initialise experience level




class Player():
    """someone who plays the game"""

    def __init__(self):
        self.exp = 1
        self.level = 0
        self.streak = 0


# self.name = input("What's your name? ")

bob = Player()

game_on = True

#sum_l is the limit for sums per level
sum_l = [9,15,25,40,60,100,500,500,1000,1000]

max_l = 8 #maximum level

level_limits = [1,20,50,150,300,700,1800,4000,9200,21000]


introduction_text = p_data["introduction"]

def play_game(Player):
    """main game loop"""

    print(introduction_text)

    questions = 3
    mission(Player, questions, sum_l, level_limits)

    while Player.level < 3:

        questions = 3

        mission(Player, questions, sum_l, level_limits)

    next_mission = 0

    while Player.level >= 3:

        questions = 5

        next_mission = mission(Player, questions, sum_l, level_limits)
            
        if next_mission == 1:
            print("Another mission opens")
            next_mission += mission(Player, questions, sum_l, level_limits)
        elif next_mission == 2:
            print("FINAL MISSION")
            mission(Player, questions, sum_l, level_limits)

play_game(bob)
