import random

def get_numbers_ticket(min = 1, max = 1000, quantity = 6):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1): #validate input
        return []
    random_list = random.sample(range(min, max + 1), quantity) #generate random values
    random_list.sort()
    return random_list

print(get_numbers_ticket(1, 100, 6)) 