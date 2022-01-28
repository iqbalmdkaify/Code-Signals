# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the
# distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

def solution(n, firstNumber):
    mid = n//2
    if firstNumber==mid:
        return 0
    if firstNumber<mid:
        return mid+firstNumber
    return firstNumber-mid
