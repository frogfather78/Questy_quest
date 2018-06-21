from random import randint
import json
import random


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
    mission(Player, questions)

    while game_on:

        questions = 5

        mission(Player, questions)

def mission(Player, questions):


    score = 0

    exp_gain = 0
    #exp_bang is how excited to get about the exp_gain
    exp_bang = ""

    for i in range(0, questions):

        z = sum_l[Player.level]
        a = randint(1, z)
        b = randint(1, z)

        print(str(a) + " + " + str(b))

        ans = input("> ")

        # cast ans to int for comparison with the correct answer
        # assuming it's a number as string...
        ans = int(ans)

#        if ans == "q":
#            # quit mission and stop playing
#            game_on = False
#            return 0
#        else:
#            #never mind

#        try:
#            ans = int(ans)
#        except NameError:
#                print("The buttons go from 0-9. Shouting doesn't work")
#                exit()
#        else:
#            #carry on?
               

        if ans == a + b:
            # correct
            print("Correct")
            score += 1
        else:
            # wrong
            print("WRONGO")

    print("You scored " + str(score) + "/" + str(questions))

    if score == questions:
        # full score, bonus marks
        exp_gain = int(z * (1 + randint(1, 5) / 20))
        exp_bang = "!!"

    elif score >= int(questions * .8):
        # 90% pass mark
        exp_gain = int(z * (randint(5, 11) / 10))
        exp_bang = "!"

    elif score >= int(questions * .5):
        # 50% not completely terrible, but NO BANG FOR YOU
        exp_gain = int(z * (randint(1, 3)) / 10)
        exp_bang = ""

    l_up_msg = ""
    #message about levelling up

    Player.exp += exp_gain
    if Player.exp > level_limits[Player.level]:
        
        l_up_msg = level_up(Player)

    print("+" + str(exp_gain) + " exp" + exp_bang)
    print(l_up_msg)
    print("\nYour exp: " + str(Player.exp) + "/" + str(level_limits[Player.level]))

def level_up(Player):
    Player.level += 1
    if Player.level == 1:
        #first level. Well done, rookie
        l_up_msg = p_data["1"]
    elif Player.level == 3:
        #the plot thickens
        l_up_msg = p_data["3"]
    elif Player.level == 5:
        #a new room
        l_up_msg = p_data["5"]
    else:
        #some other level
        l_up_msg = "\nYou're now level " + str(Player.level)
        
    return l_up_msg

play_game(bob)
