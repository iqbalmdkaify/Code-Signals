#Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    if inputString != inputString[::-1]:
        return False
    return True


#alternate solution
# import string

# def checkPalindrome(inputString):
    
#     list_str = [i for i in inputString]
#     lst_copy = list_str.copy()

#     lst_copy.reverse()
    
#     return list_str==lst_copy