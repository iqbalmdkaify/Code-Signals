#Given two strings, find the number of common characters between them.

def commonCharacterCount(s1, s2):

    counter = 0
    s2_l = [i for i in s2]

    for i in s1:
        if i in s2_l:
            rem = s2_l.index(i)
            counter += 1
            s2_l.remove(s2_l[rem])
        elif i not in s2_l:
            continue
    
    return counter

print(commonCharacterCount("abca", "xyzbac"))

#alternate solution
# def commonCharacterCount(s1, s2):
#     count  = 0
#     s1_ls, s2_ls = [i for i in s1], [i for i in s2]

#     for i in range(len(s1_ls)):
#         if s1_ls[i] in s2_ls:
#             count += 1
#             a = s2_ls.index(s1_ls[i])
#             s2_ls.pop(a)

#     return count



