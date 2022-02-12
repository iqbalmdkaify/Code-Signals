# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

def solution(text):
    f_str = ''
    map = {}
    if all([text[j].isalpha() for j in range(len(text)) if not text[j].isalpha()])==True:
        return text
    for k in range(len(text)):
        if text[k].isalpha():
            f_str+=text[k]
        elif text[k].isalpha()==False:
            map[len(f_str)] = f_str
            f_str = ''

    print(map)
    key = [keys for keys, values in map.items()]
    key.sort()
    return map[key[-1]]
        

print(solution(" "))