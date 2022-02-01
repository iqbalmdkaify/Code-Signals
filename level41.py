# Let's define digit degree of some positive integer as the number of times we need to replace 
# this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.

def solution(n):
    ls = list(map(int, [i for i in str(n)]))
    num = sum(ls)
    if len(str(n))==1:
        return 0
    elif len(str(num))==1:
        return 1
    elif len(str(num))>1:
        return 1+solution(num)