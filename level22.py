# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.
def solution(inputArray):
    count = 1
    while count<=len(inputArray):
        if all([k%count!=0 for k in inputArray]):
            return count
        count+=1
    return inputArray[-1]+1

print(solution([1, 4, 10, 6, 2]))

#  alt solution

# def solution(inputArray):
    
#     res = [i for i in range(2, max(inputArray)+2) if all([j%i!=0 for j in inputArray])]
    
#     return min(res)