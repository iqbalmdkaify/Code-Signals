# Given array of integers, remove each kth element from it.

def solution(inputArray, k):
    n = 1
    rm = []
    while ((n*k)-1)<len(inputArray):
        rm.append(inputArray[(n*k)-1])
        n+=1
    for i in range(len(rm)):
        inputArray.remove(rm[i])

    return inputArray    
