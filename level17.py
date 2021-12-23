# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def solution(inputArray):
    counter = 0
    for i in range(len(inputArray)-1):
        
        if inputArray[i+1] < inputArray[i]:
            diff = inputArray[i] - inputArray[i+1]
            counter+=(diff+1)
    return counter

    
print(solution([-1000, 0, -2, 0]))



