#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:37:34 2019

@author: ericedge
"""

def func(x):
    return x**2-4*x-7

def derfunc(x):
    return 2*x-4

def NewtonRhapson(x):
    while(abs(func(x)/derfunc(x))>=0.00001):
        x= x-func(x)/derfunc(x)
    
    print("the root is {}".format(x))

x0= 5
NewtonRhapson(x0)