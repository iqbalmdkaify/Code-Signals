# Some phone usage rate may be described as follows:

# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the neaminute_at integer) you can have?

def solution(min1, min2_10, min11, s):
    count = 0
    if s>=min1:
        count+=1
        minute_a = s-min1
        if minute_a>=(min2_10*9):

            minute_b = minute_a//(min2_10*9)
            count+=9
            if minute_a-(min2_10*9)>=min11:
                minute_c = (minute_a-(min2_10*9))//min11
                count+=minute_c

        elif minute_a<(min2_10*9):
            count+=minute_a//min2_10
            
    return count