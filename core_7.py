# One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer
# automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.

# When you finally decide to head back, you realize there's a chance the bridges on your route home are up,
# leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is.
# All you know thanks to the bike's timer is that n minutes have passed since 00:00.

# Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.

def solution(n):
    if n%60==0:
        return sum(list(map(int, str(n//60))))
    elif n%60!=0:
        ls = n-((n//60)*60)
        res = list(map(int, str(ls)))
        return sum(res) + sum(list(map(int, str(n//60))))

#  alt solution

# def solution(n):
#     val, ans = 0, 0
#     temp, length = 0, 0
#     if n%60==0:
#         val = n/60
#         length = len(str(val))
#         if length == 1:
#             return val
#         elif length>1:
#             val = str(int(val))
#             val = list(map(int,[i for i in val]))
#             return sum(val)
            
#     elif n%60!=0:
#         val = int(n//60)
#         ans = val*60
#         temp = str(int(n-ans))
#         val = str(val)
#         val = list(map(int,[i for i in val]))
#         temp = list(map(int,[i for i in temp]))
        
#         return sum(val) + sum(temp)
