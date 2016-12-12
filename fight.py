from quester import Quester
from monster import Monster
import dice as d

def fight(quester, monster):
	"""just battering each other, basically"""
	while quester.hp > 0:
		if (d.roll(10) * quester.strength) > (d.roll(10) * monster.strength):
			#quester hits monster
			monster.hp -= quester.strength
			print("Quester hits monster")
			if monster.hp <= 0:
				#monster dies, quester wins
				print("Quester beats monster!")
				quester.gain_xp(monster.level * d.roll(4))
				break
		else:
			#monster hits quester
			quester.hp -= monster.strength
			print("Monster hits quester")
			if quester.hp <= 0:
				#quester dies. oh noes
				print("Quester dies!")
				break
