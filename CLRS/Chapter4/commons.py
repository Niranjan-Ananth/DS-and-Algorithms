def print_square_matrix(mat):
    n = len(mat)
    for i in range(0, n):
        for j in range(0, n):
            print(str(mat[i][j]) + " ", end="")
        print()