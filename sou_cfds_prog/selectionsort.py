import random

def selectionsort(alist):
    for i in range(len(alist)):
        smallest= i
        for j in range(i+1,len(alist)):
            if(alist[smallest]>alist[j]):
                smallest=j
        alist[i],alist[smallest]= alist[smallest],alist[i]

alist=[]
for i in range(0,8):
    x= random.randint(1,20)
    alist.append(x)
print("unsorted list is: ", end=" ")
print(alist)
selectionsort(alist)
print("sorted list is: ", end=" ")
print(alist)
