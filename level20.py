# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def solution(inputArray):
    max = 0
    idx = 0
    while idx!=len(inputArray)-1:
        if abs(inputArray[idx]-inputArray[idx+1])>max:
            max = abs(inputArray[idx]-inputArray[idx+1])
        idx+=1
    return max
    
# alt solution

# def solution(inputArray):
    
#     num_1, num_2 = inputArray[0], inputArray[1]
    
#     for i in range(len(inputArray)-1):
        
#         if abs(inputArray[i]-inputArray[i+1]) >= abs(num_1-num_2):
#             num_1, num_2 = inputArray[i], inputArray[i+1]

#     dif = abs(num_1-num_2)

#     return dif

