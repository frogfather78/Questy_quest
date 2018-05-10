#mini plot generator nonsense

import json
import random

f_name = "plot_data.json"

plot = ""


def load_plot_data(f_name):
	try:
		with open(f_name) as f_obj:
			plot_data = json.load(f_obj)
		
	except FileNotFoundError:
		return None
	else:
		return plot_data

p_data = load_plot_data(f_name)


dude_1 = "A " + random.choice(p_data['adjective']) 

dude_1 += " " + random.choice(p_data['employment'])

dude_1 += " who is a " + random.choice(p_data['person'])


print(dude_1)

