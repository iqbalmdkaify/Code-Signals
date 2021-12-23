# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

def check(endpoint):
    if ')' in endpoint:
        return True
    return False

def reverseInParentheses(inputString):
    stack = []
    temp = [i for i in inputString]
    for i in range(len(temp)):
        if temp[i] == '(':
            stack.append(temp[i])

