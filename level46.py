# Elections are in progress!

# Given an array of the numbers of votes given to each of the candidates so far, 
# and an integer k equal to the number of voters who haven't cast their vote yet, 
# find the number of candidates who still have a chance to win the election.

# The winner of the election must secure strictly more votes than any other candidate. 
# If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

def solution(votes, k):
    if votes.count(max(votes))>1 and k==0:
        return 0
    elif k==0:
        return 1
    count = 0
    max_v = max(votes)
    for i in range(len(votes)):
        if (votes[i]+k)>max_v:
            count+=1
    
    return count


