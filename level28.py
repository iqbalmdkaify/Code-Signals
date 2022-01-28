# Given a string, your task is to replace each of its characters by the next one in the English alphabet;
# i.e. replace a with b, replace b with c, etc (z would be replaced by a).Given a string, your task is to replace
# each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

import string

def solution(inputString):
    asc_str = [j for j in string.ascii_lowercase]
    ls_s = [i for i in inputString]
    for i in range(len(ls_s)):
        idx = asc_str.index(ls_s[i])
        if idx == 25:
            ls_s[i] = asc_str[0]
        elif idx<25:
            ls_s[i] = asc_str[idx+1]
    
    return ''.join(ls_s)


# alt solution

# def solution(inputString):
#     res = []
#     org='abcdefghijklmnopqrstuvwxyz'
    
#     for i in range(len(inputString)):
#         ind = org.index(inputString[i])
#         if ind == len(org)-1:
#             ind = 0
#             res.append(org[ind])
#         elif ind<len(org):
#             res.append(org[ind+1])
    
#     return ''.join(res)



    