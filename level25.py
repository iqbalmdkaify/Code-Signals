# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i]==elemToReplace:
            inputArray[i]=substitutionElem
    
    return inputArray

# pretty

# def solution(inputArray, elemToReplace, substitutionElem):
#     return [substitutionElem if x==elemToReplace else x for x in inputArray]

# alt solution

# def solution(inputArray, elemToReplace, substitutionElem):
#     for i in range(len(inputArray)):
#         if inputArray[i]==elemToReplace:
#             inputArray[i]=substitutionElem
#         continue
    
#     return inputArray

    
