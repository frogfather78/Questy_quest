from random import randint
import json
import random

from mission import mission
from mission import level_up


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

    questions = int(p_data["questions_base"] / 3)
    mission(Player, questions, sum_l, level_limits)

    while Player.level < 3:

        questions = int(p_data["questions_base"] / 2)

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
                
          questions = p_data["questions_base"]
          #read in the quest details from the p_data file as a list
          #trophy is the final item in the quest list
          qq = random.choice(["quest1","quest2","quest3","quest4","quest5"])
          mission_msg = p_data[qq]
          #q_count the number of missions in the quest, but remember the last one is the prize
          q_count = len(mission_msg) - 1
          mission_reward = mission_msg[q_count]
          #mission_count is how many of the missions have been completed
          mission_count = 0
          
          print(mission_msg[mission_count])
          mission_win = mission(Player, questions, sum_l, level_limits)
          mission_count += mission_win
          #mission() returns 1 for full marks, so adding to mission_count
          #keeps track of where we are in quest line
          while mission_win == 1:
              print(mission_msg[mission_count])
              mission_win = mission(Player, questions, sum_l, level_limits)
              mission_count += mission_win
              
              #mission_count == q_count is the quest win!
              if mission_count == q_count:
                 Player.exp += 200
                 if Player.exp > level_limits[Player.level]:
                    #give a load of exp, check for level up
                    
                    l_up_msg = level_up(Player)
                 
                 Player.trophies.append(mission_reward)
                 print("Yo, good work, beat the quest")
                 print(l_up_msg)
                 print("\nYour exp: " + str(Player.exp) + "/" + str(level_limits[Player.level]))
                 print("\nYou gain a " + mission_reward)
                 break
                       
        elif ans == 2:
          
          questions = 10
          mission(Player, questions, sum_l, level_limits)
        
        elif ans >= 3:
          
          trophy_num = len(Player.trophies)
          print("You have " + str(trophy_num) + " trophies")
          for n in list(range(trophy_num)):
             
             print(Player.trophies[n])
             
          print("\n\n")

play_game(bob)
