# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

def solution(n):
    r_matrix = [[j for j in range(1, n+1)] for i in range(1, n+1)]

    mat = []

    for rows in range(1, n+1):
        # mat.append([])
        for cols in range(1, n+1):
            curr = cols
            mat[rows].append(curr)

    return mat

print(solution(3))

