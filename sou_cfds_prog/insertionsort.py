import random

def insertionsort(alist):
    for i in range(1,len(alist)):
        for j in range(i-1,0,-1):
            p=i
            if(alist[j]>=alist[p]):
                alist[j],alist[p]=alist[i],alist[p]
                p=j

alist=[]
for i in range(0,8):
    x= random.randint(1,20)
    alist.append(x)
print("unsorted list: ", end=" ")
print(alist)
insertionsort(alist)
print("sorted list: ", end=" ")
print(alist)
