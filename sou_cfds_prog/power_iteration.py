import numpy as np

def norma(x):
    x_1= [abs(i) for i in x]
    ind= [x_1.index(min(x_1))]
    min_1= x[ind]
    x=[i/min_1 for i in x]
    t= np.concatenate((x[0],x[1]))
    return t

def pow_iter(mat,x):
    while(True):
        x_1= np.dot(mat,x)
        if np.allclose(norma(x_1),norma(x)):
            b= norma(x_1)
            break
        x=x_1
    return b

def eig_val(A,x):
    temp= np.dot(A,x)
    tx= np.transpose(x)
    temp1= np.dot(x,tx)
    return np.dot(temp,tx)/temp1


A= np.array([[2,-12],[1,-5]])
x= np.array([[1],[1]])
eigvec= pow_iter(A,x)
eigval= eig_val(A,eigvec)
print(eigvec)
print(eigval)
