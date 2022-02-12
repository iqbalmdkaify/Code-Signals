# CodeMaster has just returned from shopping. He scanned the check of the items he 
# bought and gave the resulting string to Ratiorg to figure out the total number of purchased items.
# Since Ratiorg is a bot he is definitely going to automate it, so he needs a program
# that sums up all the numbers which appear in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

def solution(inputString):
    f_str = ''
    maps = []
    inputString+= ' '
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            f_str+=inputString[i]
        elif not inputString[i].isdigit():
            if f_str == '':
                continue
            else:
                maps.append(int(f_str))
            f_str = ''
    
    return sum(maps)