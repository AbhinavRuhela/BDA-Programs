import numpy as np
from numpy import linalg as la

def upper(mat):
    upp= mat*0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i<j:
                upp[i][j] = mat[i][j]
    return upp

def lower(mat):
    low = mat*0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>=j:
                low[i][j] = mat[i][j]
    return low

def gauss_siedel(A,x,b):
    T = -(np.dot(la.inv(lower(A)), upper(A)))
    C = np.dot(la.inv(lower(A)),b)
    while(True):
        x_1 = np.dot(T,x)+C
        if np.allclose(x_1,x):
            res = x
            break
        x = x_1
    return res

A = np.array([[16,3],[7,-11]])
b = np.array([[11],[13]])
x = np.ones(2, dtype= int).reshape(2,1)
print(gauss_siedel(A,x,b))
