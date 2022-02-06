# Given a string, find the shortest possible string which can be achieved by adding 
# characters to the end of initial string to make it a palindrome.

# def solution(st):
#     stack = []
#     idx = 0
#     if st[:]==st[::-1]:
#         return st
#     for j in range(len(st)):
        
#         if st[j] in stack:
#             stack.pop(0)
#         elif st[j] not in stack:
#             stack.append(st[j])
#         print(f'stack {stack}   itr {j}')

        
#     return stack

# print(solution("aaaabaa")) # baa

def solution(st):
    stack = []
    idx = 0
    if st[:]==st[::-1]:
        return st
    for i in range(len(st)):
        if st[i] not in stack:
            stack.append(st[i])
        idx = st.index(st[i])
        print(f'idx {idx}  {st[i]}')
        print(stack)
        
    
    print(st[idx-1::-1])
    return st+st[idx-1::-1]

print(solution("aaaaba")) # aaaaba - aaa