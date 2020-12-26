#binary search
def binsearch(a,start,end,num):
    mid= (end+start)//2
    if(end==start):
        print("not found")
    elif num==a[mid]:
        print("found {} at index {}".format(num,mid))
    else:
        if num>a[mid]:
            binsearch(a,mid,end,num)
        else:
            binsearch(a,start,mid,num)

a=[2,4,3,5,7,9,10,1,13]
#finding 10
num= 7
a= sorted(a)
n= len(a)
binsearch(a,0,n,num)
