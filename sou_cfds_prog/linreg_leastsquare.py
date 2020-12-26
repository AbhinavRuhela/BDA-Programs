import random as rndm

def least_square(x,y):
    y_sum= sum(y)
    x_sum= sum(x)
    n= len(x)
    xy= [x[i]*y[i] for i in range(n)]
    xy_sum= sum(xy)
    x2_sum= sum([i*i for i in x])
    c1= (xy_sum-(xy_sum/n))/(x2_sum-((x_sum**2)/n))
    c0= (y_sum-c1*x_sum)/n
    return c0,c1

x_val= [rndm.randint(1,30) for i in range(100)]
y_val= [rndm.randint(1,30) for i in range(100)]
x_train= x_val[:70]
y_train= y_val[:70]
x_test= x_val[70:]
y_test= y_val[70:]
c,m= least_square(x_train,y_train)
y_obt= [m*x+c for x in x_test]
error= [abs(y_obt[i]-y_test[i]) for i in range(len(x_test))]
print(error)
print()
print(sum(error)/len(error))
