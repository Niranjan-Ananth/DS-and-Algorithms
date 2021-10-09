from utils.matrix_generator import random_matrix_generator
from commons import print_square_matrix

def martix_multiply_recursive(mat_a, i1, i2, j1, j2, mat_b, k1, k2, l1, l2, mat_c):
    n = i2-i1+1 
    if n == 1:
        return mat_a[i1][j1] * mat_b[k1][l1]
    else:
        i3 = int(i2/2)
        j3 = int(j2/2)
        k3 = int(k2/2)
        l3 = int(l2/2)
        a11_b11 = martix_multiply_recursive(mat_a, i1, i3, j1, j3, mat_b, k1, k3, l1, l3, mat_c)
        a12_b21 = martix_multiply_recursive(mat_a, i1, i3, j3+1, j2, mat_b, k3+1, k2, l1, l3, mat_c)
        mat_c = a11_b11 + a12_b21
        # for i in range(i1, i3+1):
        #     for j in range(j1, j3+1):
        #         mat_c[i][j] = a11_b11[i][j] + a12_b21[i][j]
    return mat_c

if __name__=='__main__':
    n = 4
    max_limit = 100
    mat_a = random_matrix_generator(n, 10)
    mat_b = random_matrix_generator(n, 10)
    mat_c = [ [ 0 for x in range(n) ] for y in range(n) ]
    mat_c = martix_multiply_recursive(mat_a, 0, 3, 0, 3, mat_b, 0, 3, 0, 3, mat_c)
    print("Matrix A")
    print_square_matrix(mat_a)
    print("---------")
    print("Matrix B")
    print_square_matrix(mat_b)
    print("---------")
    print("Result, Matrix C")
    print_square_matrix(mat_c)
    print("---------")