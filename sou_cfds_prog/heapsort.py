import random
import time
import matplotlib.pyplot as plt

#making a heap
def insertheap(alist,n,i):
	root= i
	l= 2*i+1
	r= 2*i+2
	if(l<n and alist[i]<alist[l]):
		root= l
	if(r<n and alist[root]<alist[r]):
		root= r
	if(root!=i):
		alist[i],alist[root]= alist[root],alist[i]

		insertheap(alist,n,root)

#the main heapsort function
def heapsort(alist):
	n= len(alist)
	for i in range(n,-1,-1):
		insertheap(alist,n,i) #make a heap of elements

	for i in range(n-1,0,-1):
		alist[i],alist[0]= alist[0],alist[i] #swap the last element with the first
		insertheap(alist,i,0) #sort the heap

#create an array
def create_array(n):
	alist= random.sample(range(500),n)
	return alist

x_axis=[]
y_axis=[]
for i in range(1,500):
	alist= create_array(i)
	start= time.perf_counter()
	heapsort(alist)
	end= time.perf_counter()
	runtime= end-start
	x_axis.append(i)
	y_axis.append(runtime)
plt.plot(x_axis,y_axis)
plt.xlabel('length of array')
plt.ylabel('runtime')
