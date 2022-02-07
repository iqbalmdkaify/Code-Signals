# A media access control address (MAC address) is a unique identifier assigned to network
# interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly
# form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

import string

def check(String):
    if String.isalnum() and len(String)==2:

        ls = [i for i in String]
        r_char = [string.ascii_uppercase[j] for j in range(len(string.ascii_uppercase)) if j<6]
        num_l = list(map(str, [i for i in range(10)]))
        if (ls[0] in r_char or ls[0] in num_l) and (ls[1] in r_char or ls[1] in num_l):
            return True
        return False

    return False


def solution(inputString):
    res = []
    if len(inputString.split("-"))!=6:
        return False
    t_str = inputString.split("-")
    for i in t_str:
        if check(i):
            res.append(True)
        elif not check(i):
            res.append(False)
    
    return all(res)