# Given the positions of a white bishop and a black pawn on the standard chess board, 
# determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement. 
# Check out the example below to see how it can move:

import string

def path(b):
    cord_list = [[x-1, y+1] for x, y in range(9)]
    if b in cord_list:
        return True
    return False

def solution(bishop, pawn):
    ls = [i for i in string.ascii_lowercase]
    
    start = [i for i in bishop] 
    target = [i for i in pawn]

    b = [ls.index(start[0])+1, int(start[1])]
    c = [ls.index(target[0])+1, int(target[1])]

    # if odd y
    




    return path(b)
    
print(solution("a1", "c3"))