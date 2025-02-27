import random
from random import randint

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
print(random.choice(friends))

random_index = randint(0,4)
print(friends[random_index])