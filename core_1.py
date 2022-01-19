def solution(n):
    ls = str(n)
    temp = list(map(int, [i for i in ls]))
    return sum(temp)
