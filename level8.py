#After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def matrixElementsSum(matrix):

    counter = 0
    map = []

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0 and j not in map:
                map.append(j)
            elif col!=0 and j not in map:
                counter+=matrix[i][j]
    
    return counter

#alternate solution
# def matrixElementsSum(matrix):

#     ls = []
#     SUM = 0
        
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col]==0:
#                 ls.append(col)
#             #else
#         for i in ls:
#             matrix[row][i]=0

#     for i in matrix:
#         SUM += sum(i)

#     return SUM
                    
