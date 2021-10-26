# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

def sortByHeight(a):
    pass

a = [-1, 150, 190, 170, -1, -1, 160, 180]

indexing_length = len(a)-1
sorted = False

while not sorted:
    sorted = True
    for i in range(0,indexing_length):
        if a[i]>a[i+1] and all([a[i]!=-1, a[i+1]!=-1]):
            sorted = False
            a[i], a[i+1] = a[i+1], a[i]

print(a)

