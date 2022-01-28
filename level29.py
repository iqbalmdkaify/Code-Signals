# Given two cells on the standard chess board, determine whether they have the same color or not.

import string

def solution(cell1, cell2):
    inp = [cell1, cell2]
    res = []

    letters = [i for i in string.ascii_uppercase][0:8]
    for i in range(len(inp)):
        str = [k for k in inp[i]][0]
        num = int([j for j in inp[i]][1])

        if num%2!=0:
            if (letters.index(str)+1)%2!=0:
                res.append('dark')
            if (letters.index(str)+1)%2==0:
                res.append('light')
        elif num%2==0:
            if (letters.index(str)+1)%2!=0:
                res.append('light')
            if (letters.index(str)+1)%2==0:
                res.append('dark')

    return res[0]==res[1]
    
    

