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
        self.trophies = []


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

        questions = 2

        mission(Player, questions, sum_l, level_limits)

    next_mission = 0

    while Player.level >= 3:
        
        print("Do you want to do a quest?")
        print("1) Questy Quest!")
        print("2) Please let me do more practice stuffs")
        print("3) LIST MY TROPHIES")
        
        ans = input("> ")
        
        ans = int(ans)
        
        if ans == 1:
                
          questions = 3
          mission_msg = ['','Another mission opens','FINAL MISSIOB']
          mission_reward = 'A nice helmet'
          mission_count = 0
          
          print("Let's do a quest")
          mission_win = mission(Player, questions, sum_l, level_limits)
          mission_count += mission_win
          while mission_win == 1:
              print(mission_msg[mission_count])
              mission_win = mission(Player, questions, sum_l, level_limits)
              mission_count += mission_win
              if mission_count == 3:
                 Player.exp += 200
                 Player.trophies.append(mission_reward)
                 print("Yo, good work, beat the quest")
                 print("\nYour exp: " + str(Player.exp) + "/" + str(level_limits[Player.level]))
                 break
                       
        elif ans == 2:
          
          questions = 3
          mission(Player, questions, sum_l, level_limits)
        
        elif ans >= 3:
          print(Player.trophies)

play_game(bob)
