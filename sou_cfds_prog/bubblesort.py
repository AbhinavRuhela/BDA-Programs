import random

def bubblesort(alist):
    for i in range(len(alist)-1,0,-1):
        isswap=True
        for j in range(0,i):
            if(alist[j+1]<alist[j]):
                alist[j],alist[j+1]= alist[j+1],alist[j]
                isswap=False
                if isswap:
                    return

alist=[]
for i in range(0,8):
    x= random.randint(1,20)
    alist.append(x)
print("unsorted list: ", end=" ")
print(alist)
bubblesort(alist)
print("sorted list: ", end=" ")
print(alist)
