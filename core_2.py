# Given an integer n, return the largest number that contains exactly n digits.

def solution(n):
    return (10**n)-1


# alt solution

# def solution(n):
#     val_s = ''
#     for i in range(n):
#         val_s += '9'
#     num = int(val_s)
#     return num
    