import random

#1.-
def shuffle_list(lst):
    shuffled = lst[:]          
    random.shuffle(shuffled)   
    return shuffled

#2.-
def unique_random_numbers():
    return random.sample(range(10), 7)

print(shuffle_list([1, 2, 3, 4, 5]))   
print(unique_random_numbers())        
