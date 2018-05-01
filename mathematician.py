from random import randint

#initialise experience level

class Player():
	"""someone who plays the game"""
	def __init__(self):
		self.exp = 1
		#self.name = input("What's your name? ")

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
		
	
		if Player.exp < 11:
			mission(9, Player)
		elif Player.exp < 100:
			mission(40, Player)
		else:
			mission(99, Player)
	
	
def mission(level, Player):
		
	print("\n\nIt's an adding game")
	
	score = 0
	
	for i in range(0,10):
	
		
		a = randint(1, level)
		b = randint(1, level)
	
		print(str(a) + " + " + str(b))
	
		ans = input("> ")
		
		
		if ans == "quit":
			#quit mission and stop playing
			game_on = False
			return 0
		
		#cast ans to int for comparison with the correct answer
		ans = int(ans)
		
		elif ans == a+b:
			#correct
			print("Correct")
			score += 1
		else:
			#wrong
			print("WRONGO")
		
	print("You scored " + str(score))	
	
	if score > 9:
		#pass mark
		Player.exp += level
	
	print("Your exp: " + str(Player.exp))
		
	
	
play_game(bob)
