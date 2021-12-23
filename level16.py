# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.
a = [1, 2, 3]
b = [1, 3, 2]

def solution(a, b):
    pass



print(solution(a, b))

# alternate solution

# def solution(a, b):

#     swap = []
    
#     if len(a)!=len(b):
#         return a!=b
#     elif len(a)==len(b):
#         for i in range(len(a)):
#             if a[i]!=b[i]:
#                 swap.append(i)
#         if len(swap)==0:
#             return a==b
#         while len(swap)>1:
#             for i in range(len(swap)-1): #swapping in b for indices in swap
#                 b[swap[i]], b[swap[i+1]] = b[swap[i+1]], b[swap[i]]
#                 if a==b:
#                     return a==b
#                 b[swap[i]], b[swap[i+1]] = b[swap[i+1]], b[swap[i]]
#             return a==b
