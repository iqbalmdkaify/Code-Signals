# Find the leftmost digit that occurs in a given string.

def solution(inputString):
    for j in inputString:
        if j.isdigit():
            res = j
            break

    return res
