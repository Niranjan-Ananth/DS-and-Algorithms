import random

def random_number_generator(n):
    random_number = int(random.random() * n)
    return random_number

def random_matrix_generator(n, max_limit):
    matrix = [[0]*n for i in range(n)]   
    for i in range(0, n):
        for j in range(0, n):
            num = random_number_generator(max_limit)        
            matrix[i][j] = num
    return matrix
