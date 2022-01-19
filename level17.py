# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def solution(inputArray):
    counter = 0

    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            diff = inputArray[i] - inputArray[i+1]
            counter+=(diff+1)
            inputArray[i+1] = inputArray[i+1] + diff + 1


    return counter

# alternate solution

# def solution(inputArray):
    
#     #[1, 1, 1], exactly one chance +1 per move
#     #find minimal number of moves
#     moves_min = 0

#     for i in range(len(inputArray)-1):
#         if inputArray[i]<inputArray[i+1]:
#             continue
#         else:
#             while inputArray[i]>=inputArray[i+1]:

#                 moves_min += (inputArray[i]-inputArray[i+1])+1
#                 inputArray[i+1] += (inputArray[i]-inputArray[i+1])+1
                
#     return moves_min



