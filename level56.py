# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.


def solution(product):
    maps = {}
    f_str = ''
    min_l = product
    
    if len(str(product))==1 and product>0:
        return int("1"+str(product))
    for k in range(1, 10):
        if product%k!=0:
            continue
        elif product%k==0:
            n = int(str(k)+str(product//2))
            if n<min_l:
                f_str += str(k)+str(product//2)
                min_l = n

    

    return f_str

print(solution(12))
