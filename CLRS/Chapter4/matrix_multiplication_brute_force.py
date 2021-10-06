from utils.matrix_generator import random_matrix_generator

def martix_multiply(mat_a, mat_b):
    return mat_a    

if __name__=='__main__':
    n = 16
    max_limit = 100
    mat_a = random_matrix_generator(n, 100)
    mat_b = random_matrix_generator(n, 100)
    mat_c = martix_multiply(mat_a, mat_b)
    for i in range(0, n):
        for j in range(0, n):
            print(mat_c[i][j] + " ", end="")
        print()
