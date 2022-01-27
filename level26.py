# Check if all digits of the given integer are even.

def solution(n):
    n_n = list(map(int, [i for i in str(n)]))
    res = False
    for i in range(len(n_n)):
        if n_n[i]%2!=0:
            res = False
            break
        res = True
    return res

# alt solution

# def solution(n):
    # res = True
    # mapped = list(map(int,[i for i in str(n)]))
    # for i in range(len(mapped)):
    #     if mapped[i]%2!=0:
    #         res = False
    #         break
    #     res = True
    # return res
