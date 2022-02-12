# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.


def solution(s):
    res = ''
    curr = s[0]
    f_str = ''
    for i in range(len(s)):
        if s[i]!=curr:
            curr = s[i]
            res+='-'
        res+=s[i]
    t = res.split('-')

    for i in range(len(t)):
        if len(t[i])>1:
            f_str+=str(len(t[i]))+str(t[i][0])
        elif len(t[i])==1:
            f_str+=t[i]
        
    return f_str