# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.


def solution(matrix):

    r_mat = []
    count = 0

    for j in range(len(matrix)):
        r_mat.append([])
        nest = r_mat[j]
        for k in range(len(matrix[j])):

            # 2nd loop
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):


                    if any([(row==j), (row==j+1), (row==j-1)]) and any([(col==k), (col==k+1), (col==k-1)]):

                        if matrix[row][col]==1 and (row, col)!=(j, k):
                            count+=1
                            print(f' found:    x {row}   y {col}\n')

            print(f'row {j}   col {k}    count {count}')
            nest.insert(k, count)
            count = 0

            
            


    return r_mat
                    




print(solution([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]))
