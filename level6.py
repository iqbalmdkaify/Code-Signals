#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
    max_n, min_n = max(statues), min(statues)
    counter, last = 0, 0
    temp = max_n

    while temp != min_n:
        if temp in statues:
            temp -=1
        elif temp not in statues:
            counter += 1
            temp -=1
    return counter

#alternate solution
# def makeArrayConsecutive2(statues):
    
#     statues.sort()
#     start =min(statues)
#     end = max(statues)
    
#     temp = [i for i in range(start,end+1)]
#     count = 0
    
#     for i in temp:
#         if i not in statues:
#             count+=1
            
#     return count
    