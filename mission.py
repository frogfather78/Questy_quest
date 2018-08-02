from random import randint, randrange
import json
import random

def mission(Player, questions, sum_l, level_limits):


    score = 0

    exp_gain = 0
    #exp_bang is how excited to get about the exp_gain
    exp_bang = ""

    full_marks = 0

    for i in range(0, questions):

        z = sum_l[Player.level]
        a = randint(1, z)
        b = randint(1, z)

        print(str(a) + " + " + str(b))

        ans = input("> ")

        # cast ans to int for comparison with the correct answer
        # assuming it's a number as string...
        ans = int(ans)
           

        if ans == a + b:
            # correct
            print("Correct")
            score += 1
            Player.streak += 1
        else:
            # wrong
            print("Wrong")
            Player.streak = 0
        
        streak_msg = check_streak(Player)
        print(streak_msg)
    
    print("You scored " + str(score) + "/" + str(questions))

    if score == questions:
        # full score, bonus marks
        exp_gain = int(z * (1 + randint(1, 5) / 20))
        exp_bang = "!!"
        full_marks = 1

    elif score >= int(questions * .8):
        # 80% pass mark
        exp_gain = int(z * (1 + randrange(-2, 3) / 10))
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

    return full_marks



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
    elif Player.level == 6:
        #the truth!
        l_up_msg = p_data["6"]
    else:
        #some other level
        l_up_msg = "\nYou're now level " + str(Player.level)
        
    return l_up_msg
    
def check_streak(Player):
    if Player.streak == 10:
        Player.trophies.append("X")
        return "Streak 10!"
    elif Player.streak == 50:
        Player.trophies.append("Half centurion")
        return "Streak 50!!"
    elif Player.streak == 100:
        Player.trophies.append("The Ton")
        return  "STREAK 100!!"
    else:
        return ""

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

