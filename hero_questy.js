#import json

#load plot and level up text into p_data
f_name = "hero_plot.json"


def load_plot_data(f_name):

	try:
		with open(f_name) as f_obj:
			plot_data = json.load(f_obj)

	except FileNotFoundError:
		return None
	else:
		return plot_data

p_data = load_plot_data(f_name)

class Player():
    """someone who plays the game"""

    def __init__(self):
        self.exp = 0
        self.level = 1
        self.trophies = []


# self.name = input("What's your name? ")

bob = Player()

game_on = True

max_l = 8 #maximum level

level_limits = [1,20,50,150,300,700,1800,4000,9200,21000]


introduction_text = p_data["introduction"]

def play_game(Player):
    """main game loop"""

    print(introduction_text)
    print(Player.level)

play_game(bob)
