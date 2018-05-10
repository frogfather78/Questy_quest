#mini plot generator nonsense

import json
import random

plot = ""

#adjective, employment, person

adjective = ["sweaty", "pale", "hirsute"]

employment = ["Postie", "Factory owner", "Brewer"]

person = ["Man", "Woman", "Non-binary teenager"]

dude_1 = "A " + random.choice(adjective) + " " + random.choice(employment)

dude_1 += " who is a " + random.choice(person)


print(dude_1)

