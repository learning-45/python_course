import random 

random.seed(1)

def print_random():
    for i in range(5):
        print(random.randint(1, 100), end = " ")

print_random()