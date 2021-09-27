import random

def random_number_generator(n):
    random_number = int(random.random() * n)
    return random_number

def random_array_generator(n, max_limit):    
    s = set()
    while len(s) < n:
        num = random_number_generator(max_limit)        
        if num not in s:
            s.add(num)
    return list(s)
    
def sorted_array_generator(n, max_limit):
    arr = random_array_generator(n, max_limit)
    arr.sort()
    return arr