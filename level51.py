# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

def solution(n):
    ls = list(map(int, [i for i in str(n)]))
    max_n, i = 0, 0
    while i<len(list(map(int, ls))):
        e = ls.pop(i)
        if int(''.join(list(map(str, ls))))>max_n:
            max_n = int(''.join(list(map(str, ls))))
        ls.insert(i, e)
        i+=1
    
    return max_n