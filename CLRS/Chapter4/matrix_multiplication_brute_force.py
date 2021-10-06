from utils.matrix_generator import random_matrix_generator
from commons import print_square_matrix

def martix_multiply(mat_a, mat_b):
    n = len(mat_a)
    mat_c = [ [ 0 for i in range(n) ] for j in range(n) ]
    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                sum += mat_a[i][k] * mat_b[k][j]
            mat_c[i][j] = sum
    return mat_c

if __name__=='__main__':
    n = 4
    max_limit = 100
    mat_a = random_matrix_generator(n, 10)
    mat_b = random_matrix_generator(n, 10)
    mat_c = martix_multiply(mat_a, mat_b)
    print("Matrix A")
    print_square_matrix(mat_a)
    print("---------")
    print("Matrix B")
    print_square_matrix(mat_b)
    print("---------")
    print("Result, Matrix C")
    print_square_matrix(mat_c)
    print("---------")