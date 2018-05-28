from random import randint

#branch: level-up

# initialise experience level

class Player():
    """someone who plays the game"""

    def __init__(self):
        self.exp = 1


# self.name = input("What's your name? ")

bob = Player()

game_on = True

introduction_text = "You're in a room with a row of ten dusty lightbulbs"

introduction_text += ". It doesn't look like anyone has been in here"

introduction_text += " for some time. A row of buttons is set in the "

introduction_text += "top of the counter. The bulbs and keys are numbered"

introduction_text += " 0 to 9. One of the bulbs lights up and then "

introduction_text += "another."


def play_game(Player):
    """main game loop"""

    print(introduction_text)

    while game_on:

        questions = 3

        if Player.exp < 11:
            mission(9, Player, questions)
        elif Player.exp < 100:
            mission(40, Player, questions)
        else:
            mission(99, Player, questions)


def mission(level, Player, questions):
    print("\n\nIt's an adding game")

    score = 0


    exp_gain = 0
    #exp_bang is how excited to get about the exp_gain
    exp_bang = ""

    for i in range(0, questions):

        a = randint(1, level)
        b = randint(1, level)

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
        exp_gain = int(level * (1 + randint(1, 5) / 20))
        exp_bang = "!!"

    elif score >= int(questions * .9):
        # 90% pass mark
        exp_gain = int(level * (randint(5, 11) / 10))
        exp_bang = "!"

    elif score >= int(questions * .5):
        # 50% not completely terrible, but NO BANG FOR YOU
        exp_gain = int(level * (randint(1, 3) / 10))
        exp_bang = ""

    Player.exp += exp_gain

    print("+" + str(exp_gain) + " exp" + exp_bang)
    print("Your exp: " + str(Player.exp))

play_game(bob)
