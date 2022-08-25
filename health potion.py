import random
health = 50
# dificulty level varies from 1 to 3 where 1 being easy and 3 being hard
difficulty = 3
potion_health = int(random.randint(25, 50)/difficulty)
health = health + potion_health
print(health)