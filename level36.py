# Given a string, find the number of different characters in it.

def solution(s):
    map_s = []
    for i in range(len(s)):
        if s[i] in map_s:
            continue
        map_s.append(s[i])
    
    return len(map_s)
