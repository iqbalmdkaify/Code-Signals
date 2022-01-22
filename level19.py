# Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    
    if (yourLeft+yourRight)==(friendsLeft+friendsRight) and any([
        yourLeft==friendsLeft, 
        yourRight==friendsRight,
        yourLeft==friendsRight,
        yourRight==friendsLeft
        ]):
        return True
    return False


# alt solution

# def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    
#     if yourLeft == friendsLeft and yourRight == friendsRight:
#         return True
#     elif yourLeft == friendsRight and yourRight == friendsLeft:
#         return True
#     return False