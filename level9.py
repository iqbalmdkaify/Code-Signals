#For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    map = []
    counter, max_elm = 0, 0
    
    for i, word in enumerate(inputArray):
        for j in word:
            counter += 1
        if counter > max_elm:
            max_elm = counter
            map = []
            map.append(word)
        elif counter == max_elm:
            map.append(word)
        counter = 0

    return map

#alternate solution
# def allLongestStrings(inputArray):
#     max_str_len = len(inputArray[0])
    
#     for i in range(len(inputArray)):
#         if len(inputArray[i])>max_str_len:
#             max_str_len = len(inputArray[i])
#     res = [strings for strings in inputArray if len(strings==max_str_len]
        
#     return res