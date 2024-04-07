#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

from linalglib import LinAlgLib as la

A = la.Matrix(content=[[1,2,3],[4,5,6]])
print(A.transpose())
print(A)