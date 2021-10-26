# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half. Given a ticket number (n), determine if it's lucky or not.

def isLucky(n):
    st = str(n)
    l = [i for i in st]
    nums = [int(i) for i in l]
    half_ln =int( len(nums)/2)

    return sum(nums[:half_ln])==sum(nums[half_ln:])

#alternate solution
# def isLucky(n):
#     string_n = str(n)
#     str_list = [i for i in string_n]
#     num = list(map(int,str_list))
#     length = len(num)
#     mid_index = length//2
    
#     l_sum, r_sum = sum(num[:mid_index]), sum(num[mid_index:])
    
#     return l_sum == r_sum

#map() method is important for converting elements in list
