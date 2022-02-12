# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.


def solution(matrix):
    maps = []
    count = 0

    for k in range(len(matrix)-1):
        for j in range(len(matrix[k])-1):
            s_m = [
                [matrix[k][j], matrix[k][j+1]],
                [matrix[k+1][j], matrix[k+1][j+1]]
            ]
            if s_m not in maps:
                maps.append(s_m)
                count += 1
            elif s_m in maps:
                continue

    return count