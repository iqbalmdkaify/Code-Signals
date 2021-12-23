# Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

def solution(a):
    res = 0
    for x in range(len(a)):
        if x%2!=0:
            res += a[x]
    return [sum(a)-res, res]

# alternate solution

# def solution(a):
    
#     ls_1, ls_2 = [], []
#     SUM = []
#     counter = 0
#     if len(a)%2!=0:
#         a.append(0)
#     if len(a) == 1:
#             return [a[0], 0]
            
#     else:
#         for i in range(0,len(a)-1,2):
#             print(a[i+1],a[i])
#             ls_2.append(a[i+1])
#             ls_1.append(a[i])

#         SUM.append(sum(ls_1))
#         SUM.append(sum(ls_2))
        
#         return SUM