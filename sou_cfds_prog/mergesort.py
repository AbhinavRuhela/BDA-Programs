import random

def merge(left,right):
    result= []
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(alist):
    if(len(alist)<=1):
        return alist
    mid= int(len(alist)/2)
    left= mergesort(alist[:mid])
    right= mergesort(alist[mid:])
    return merge(left,right)

alist=[]
for i in range(0,8):
    x= random.randint(1,20)
    alist.append(x)
print("unsorted list is as follows:", end= " ")
print(alist)
print("sorted list is as follows:", end= " ")
print(mergesort(alist))
