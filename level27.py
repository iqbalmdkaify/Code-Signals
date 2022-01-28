# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

def solution(name):
    res = []
    if name == "":
        return False
    for i in range(len(name)):
        
        if i==0:
            if name[0].isdigit() or name[0].isspace():
                res.append(False)
        elif i>0:
            if name[i]=='_' or name[i].isalnum():
                res.append(True)
            elif name[i]!='_' or not(name[i].isalnum()) or name[i].isspace():
                res.append(False)
        
    
    return all(res)