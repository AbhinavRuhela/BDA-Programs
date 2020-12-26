import random

def quickSort(alist):
    quickSortp(alist,0,len(alist)-1)

def quickSortp(alist,first,last):
    if(first < last):
        splitpoint = partition(alist,first,last)
        quickSortp(alist,first,splitpoint-1)
        quickSortp(alist,splitpoint+1,last)

def partition(alist,first,last):
    low=high=first
    while(high<last):
        if(alist[high]<=alist[last]):
            alist[high], alist[low]= alist[low],alist[high]
            low+=1
        high+=1
    alist[low],alist[last]= alist[last],alist[low]
    return low

alist=[]
for i in range(0,8):
    x= random.randint(1,20)
    alist.append(x)
print("unsorted list: ", end=" ")
print(alist)
quickSort(alist)
print("sorted list: ", end=" ")
print(alist)
