# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

def sortByHeight(a):
    pass

a = [-1, 150, 190, 170, -1, -1, 160, 180]

itr_a, itr_b, next = a[0], a[0], a[0]

for i in range(len(a)+1):
    if a[i] == -1:
        itr_a = a[i]
    elif a[i]!=-1:
        itr_b = a[i]
        if a[i+1]!=-1 and a[i]!=a[-1]:
            if a[i+1]>itr_b:
                a[i], a[i+1] = a[i+1], a[i]
print(a)

