# Given a string, output its longest prefix which contains only digits.


def solution(inputString):
    stack = []
    if inputString[0]== " ":
        return ""
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            stack.append(inputString[i])
        elif inputString[i].isalpha():
            break
        
    return "".join(stack)