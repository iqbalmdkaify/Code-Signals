# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    sym = '*'
    length = len(picture[0])
    res = []
    for x in range(len(picture)):
        res.append(sym+picture[x]+sym)
    res.insert(0, sym*(length+2))
    res.insert(len(picture)+1, sym*(length+2))
    return res

# alternate solution

# def solution(picture): 
    
#     items = []
#     changed = ''
#     for i in range(len(picture)):
#         ch = '*' * int(len(picture[i])+2)

#         changed += '*' + picture[i] + '*'
#         items.append(changed)
#         changed = ''
    
#     items.insert(0, ch)
#     items.append(ch)

#     return items
