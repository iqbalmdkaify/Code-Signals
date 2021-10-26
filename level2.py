#Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    rem = year % 100

    if rem != 0:
        return (int(year//100) + 1)
    return int(year//100)

    #alternate solution:-

    # cen = [i for i in range(1,3000,100)]
    
    # for i in range(len(cen)):
    #     if year<cen[i]:
    #         res = i
    #         break
        
    # return res