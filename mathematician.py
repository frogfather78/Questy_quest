from random import randint

#branch: level-up

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
sum_l = [10,15,18,22,25,37,50,60,78,100]

max_l = 8 #maximum level

level_limits = [1,20,50,150,300,700,1800,4000,9200,21000]


introduction_text = "You're in a room with a row of ten dusty lightbulbs"

introduction_text += ". It doesn't look like anyone has been in here"

introduction_text += " for some time. A row of buttons is set in the "

introduction_text += "top of the counter. The bulbs and keys are numbered"

introduction_text += " 0 to 9. One of the bulbs lights up and then "

introduction_text += "another."


def play_game(Player):
    """main game loop"""

    print(introduction_text)

    questions = 3
    mission(Player, questions)

    while game_on:

        questions = 6

        mission(Player, questions)

def mission(Player, questions):
    print("\n\nIt's an adding game")

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

        if ans == "quit":
            # quit mission and stop playing
            game_on = False
            return 0



        elif ans == a + b:
            # correct
            print("Correct")
            score += 1
        else:
            # wrong
            print("WRONGO")

    print("You scored " + str(score))

    if score == questions:
        # full score, bonus marks
        exp_gain = int(z * (1 + randint(1, 5) / 20))
        exp_bang = "!!"

    elif score >= int(questions * .9):
        # 90% pass mark
        exp_gain = int(z * (randint(5, 11) / 10))
        exp_bang = "!"

    elif score >= int(questions * .5):
        # 50% not completely terrible, but NO BANG FOR YOU
        exp_gain = int(z * (randint(1, 3) / 10))
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
        l_up_msg = "\n\nAn old man enters the room with the dusty lightbulbs."
        l_up_msg += " He hands you a card with a big 1 on it."
        l_up_msg += " \n'You're now Level 1,' he says. 'You can come through.'"
        l_up_msg += " \nHe brings you into a room with a similar machine,"
        l_up_msg += " but much less dusty."
    elif Player.level == 3:
        #the plot thickens
        l_up_msg = "\n\nThe old man pops into the room."
        l_up_msg += "\n'You might have noticed the questions getting harder.'" 
        l_up_msg += "\n'I'll come back if you get to level 5.'"
        l_up_msg += "\n\nYou're now level 3."
    else:
        #some other level
        l_up_msg = "\nYou're now level " + str(Player.level)
        
    return l_up_msg

play_game(bob)
