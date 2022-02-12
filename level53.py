# Check if the given string is a correct time representation of the 24-hour clock.

def solution(time):
    ls = list(map(int, time.split(":")))
    if ls[0] in range(0, 24) and ls[1] in range(1, 60):
        return True
    return False