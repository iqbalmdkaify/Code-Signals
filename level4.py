#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    max_product = inputArray[0]*inputArray[1]

    for i in range(0,len(inputArray)-1,1):
        product = inputArray[i]*inputArray[i+1]

        if product > max_product:
            max_product = product
    return max_product

#alternate solution
# def adjacentElementsProduct(inputArray):
    
#     res = []

#     for i in range(len(inputArray)-1):
#         val = inputArray[i]*inputArray[i+1]
#         res.append(val)

#     result = max(res)

#     return result