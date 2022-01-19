# Given a divisor and a bound, find the largest integer N such that:

# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.

def solution(divisor, bound):
    if bound%divisor==0:
        return bound
    while bound%divisor!=0:
        bound-=1
    return bound

#  alt solution

# def solution(divisor, bound):
    
#     if bound%divisor == 0:
#         return bound
#     while bound%divisor!=0:
#         bound-=1
#     return bound
