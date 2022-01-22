# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any
# two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

def solution(n, firstNumber):
    bound = n//2
    if firstNumber>bound:
        return firstNumber-bound
    elif firstNumber==bound:
        return 0
    return firstNumber+bound

#  alt solution

# def solution(n, firstNumber):
#     mid_point = n//2
#     if firstNumber>mid_point:
#         return mid_point-(n-firstNumber)
#     elif firstNumber==mid_point:
#         return 0
#     return mid_point+firstNumber