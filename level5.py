#Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the (n - 1) interesting polygon and appending 1-interesting polygons to its rim, side by side.

def shapeArea(n):
    get = n-1
    return (((n+get)*(n+get)) + 1)/2

#alternate solution
# def shapeArea(n):

#     temp = n-1
    
#     N = n+temp
    
#     val = (N*N)+1
#     area = val/2
#     return area